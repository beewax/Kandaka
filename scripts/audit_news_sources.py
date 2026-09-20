"""Read-only source probe; JSON output includes real feed and relevant-item counts."""
import concurrent.futures
import json
import sys
import fetch_news as news


def probe(pair):
    name, url = pair
    result = dict(id=name, url=url)
    raw = news.fetch_feed(url, timeout=15)
    try:
        items = news.parse_feed(raw) if raw else []
        relevant = [x for x in items if news.classify_sudan_relevance(x['title'], news.clean_text(x['description'])[:420])[0]]
        result.update(items=len(items), relevant=len(relevant), sample=[dict(title=x['title'], published=x['published']) for x in relevant[:2]])
    except Exception as exc:
        result['error'] = str(exc)
    return result

if __name__ == '__main__':
    pairs = [(s['id'], s['url']) for s in news.load_sources() if s.get('url')]
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        results = list(pool.map(probe, pairs))
    with open(sys.argv[1], 'w', encoding='utf-8') as out:
        json.dump(results, out, ensure_ascii=False, indent=2)
    for r in results:
        print(r['id'], r.get('items', 0), r.get('relevant', 0), r.get('error', ''))
