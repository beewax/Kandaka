# Pinterest RSS feeds

Kandaka publishes image-rich RSS 2.0 feeds for Pinterest from each content section.

Recommended connections:

- `https://kandaka.com/images/pinterest.xml` → Sudan Maps, Archaeology & Historic Images
- `https://kandaka.com/ideas/pinterest.xml` → Sudan's Future: Cities, Water & Infrastructure

The economic-development and other boards remain in the reviewed weekly workflow until their Kandaka sections consistently provide suitable non-cover images.

The feed template:

- includes only entries with an image;
- emits Pinterest-compatible `media:content` metadata;
- removes duplicate image URLs within each feed;
- excludes the library section to prevent book covers from being published;
- supports `pinterest_exclude: true` in front matter for any item that should never become a Pin;
- limits each section feed to its newest 100 unique images.

Historical images extracted from Nile Bookstore editions continue through the reviewed weekly workflow rather than unattended RSS publishing.
