import datetime as dt
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import fetch_news as news

NOW = dt.datetime(2026, 9, 20, 18, tzinfo=dt.timezone.utc)

def story(n, publisher='A', lang='en', age=0, source_class='sudanese_journalism'):
    return dict(title=f'Sudan report {n}', description='', link=f'https://example.com/{lang}/{n}',
                lang=lang, source=publisher, source_id=publisher, publisher=publisher,
                source_class=source_class, topic='Health', geography=['Khartoum'],
                published=NOW-dt.timedelta(days=age), status='Reporting', cluster_id=str(n),
                image='', media_reuse_basis='', author='')

class DiversityTests(unittest.TestCase):
    def test_opening_three_have_distinct_publishers(self):
        items = [story(i) for i in range(20)] + [story(30, 'B'), story(31, 'C')]
        selected = news.select_balanced(items)
        self.assertEqual(len({s['publisher'] for s in selected[:3]}), 3)
        self.assertLessEqual(sum(s['publisher']=='A' for s in selected), 2)

    def test_institution_cap(self):
        selected = news.select_balanced([story(i, str(i), source_class='official') for i in range(10)])
        self.assertEqual(len(selected), 3)

    def test_two_publishers_still_get_second_cards(self):
        selected = news.select_balanced([story(1), story(2), story(3, 'B'), story(4, 'B')])
        self.assertEqual(len(selected), 4)

    def test_similar_headlines_group_but_different_numbers_do_not(self):
        a = story(1)
        b = story(2, 'B')
        a['title'] = 'Sudan hospital reopens maternity ward in Khartoum city'
        b['title'] = 'Hospital reopens maternity ward in Khartoum city today'
        self.assertTrue(news.same_story(a, b))
        a['title'] += ' 12'
        b['title'] += ' 24'
        self.assertFalse(news.same_story(a, b))

    def test_culture_and_health_not_swallowed_by_war_context(self):
        self.assertEqual(news.classify_topic("Darfur photographer focusing on love in Sudan's war", 'Sudan News'), 'Culture')
        self.assertEqual(news.classify_topic('Sudan healthcare system near collapse', 'Sudan News'), 'Health')

    def test_languages_do_not_collapse(self):
        snapshot = news.build_snapshot([story(1), story(1, lang='ar')], NOW)
        self.assertEqual(len(snapshot['en']['latest']), 1)
        self.assertEqual(len(snapshot['ar']['latest']), 1)

    def test_latest_limit_cannot_exclude_other_publishers_from_balanced(self):
        items = [story(i) for i in range(155)] + [story(200, 'B', age=1)]
        snapshot = news.build_snapshot(items, NOW)
        self.assertEqual(len(snapshot['en']['latest']), 150)
        self.assertIn('B', {c['Params']['source'] for c in snapshot['en']['balanced']})

    def test_tracking_links_deduplicated(self):
        one = story(1)
        two = dict(one, link=one['link']+'?utm_source=rss', cluster_id='other')
        self.assertEqual(len(news.build_snapshot([one, two], NOW)['en']['latest']), 1)

    def test_stale_future_and_undated_excluded(self):
        undated = dict(story(4), published=news.parse_date(None))
        snapshot = news.build_snapshot([story(1), story(2, age=31), story(3, age=-1), undated], NOW)
        self.assertEqual(len(snapshot['en']['latest']), 1)

    def test_white_house_is_not_kordofan(self):
        title = 'البيت الأبيض يعلن محادثات جديدة مع إيران'
        self.assertFalse(news.classify_sudan_relevance(title)[0])
        self.assertEqual(news.classify_geography(title), ['National'])

    def test_island_and_shared_nile_do_not_establish_sudan_context(self):
        self.assertFalse(news.classify_sudan_relevance('كوبا: عودة الكهرباء', 'تكافح الجزيرة الحصار')[0])
        self.assertFalse(news.classify_sudan_relevance('جنوب السودان: لسنا خائفين من بناء سدود على نهر النيل')[0])
        self.assertTrue(news.classify_sudan_relevance('افتتاح مدارس جديدة في ولاية الجزيرة')[0])

    def test_warn_is_not_war(self):
        self.assertEqual(news.classify_topic('Sudan doctors warn of cholera outbreak', 'Sudan News'), 'Health')

    def test_quota_applied_after_filtering(self):
        source = dict(id='test', name='Test', lang='en', source_class='international_journalism', filter=True, max_items=1, media_policy='rss_metadata', url='https://example.com/rss')
        xml = b'<rss><channel><item><title>Unrelated news</title><link>https://example.com/a</link></item><item><title>Sudan news</title><link>https://example.com/b</link></item></channel></rss>'
        with patch.object(news, 'fetch_feed', return_value=xml):
            items, health = news.collect_source(source)
        self.assertEqual(len(items), 1)
        self.assertEqual(health['status'], 'ok')

    def test_archive_filename_preserved_when_title_changes(self):
        item = story(1)
        item.update(related_sources=[], corroboration_count=1)
        with tempfile.TemporaryDirectory() as folder:
            original = Path(folder)/'original.en.md'
            news.write_candidate(item, Path(folder), existing_path=original)
            self.assertTrue(original.exists())
            self.assertEqual(len(list(Path(folder).glob('*.md'))), 1)

if __name__ == '__main__':
    unittest.main()
