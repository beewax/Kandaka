import json
import os
from anthropic import Anthropic

# Read API key from separate file
with open("api_key.txt", "r") as f:
    API_KEY = f.read().strip()

client = Anthropic(api_key=API_KEY)

# Load library - use utf-8-sig to handle BOM
with open("data/library.json", "r", encoding="utf-8-sig") as f:
    library = json.load(f)

# Process books without descriptions
books_missing = [b for b in library["books"] if not b.get("desc")]
print(f"Generating descriptions for {len(books_missing)} books...")

for i, book in enumerate(books_missing):
    prompt = f"Write a one-sentence English description (20-30 words) for this academic work about Sudan: Title: {book['title']} Author: {book['author']} Tags: {', '.join(book.get('tags', [])) if book.get('tags') else 'Sudan studies'} Description:"

    response = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=60,
        temperature=0.7,
        messages=[{"role": "user", "content": prompt}]
    )
    
    book["desc"] = response.content[0].text.strip()
    print(f"OK [{i+1}/{len(books_missing)}] {book['title'][:50]}...")

# Save without BOM
with open("data/library.json", "w", encoding="utf-8") as f:
    json.dump(library, f, ensure_ascii=False, indent=2)

print(f"Done! Added {len(books_missing)} descriptions")