import re

path = "C:\\Users\\Abdulla\\Kandaka\\scripts\\fetch_news.py"

with open(path, encoding="utf-8") as f:
    content = f.read()

old = """def is_sudan_relevant(title, desc=""):
    title_lower = (title or "").lower()
    desc_lower = (desc or "").lower()
    for kw in SUDAN_KEYWORDS:
        if kw in title_lower:
            return True
    for kw in SUDAN_AR:
        if kw in (title or "") or kw in (desc or ""):
            return True
    for kw in SUDAN_KEYWORDS:
        pattern = r'\\\\b' + re.escape(kw) + r'\\\\b'
        if re.search(pattern, desc_lower):
            return True
    return False"""

new = """def is_sudan_relevant(title, desc=""):
    # Title-only matching prevents off-topic stories slipping through via description
    title_lower = (title or "").lower()
    for kw in SUDAN_KEYWORDS:
        if kw in title_lower:
            return True
    for kw in SUDAN_AR:
        if kw in (title or ""):
            return True
    return False"""

if old in content:
    content = content.replace(old, new)
    print("Pattern found and replaced.")
else:
    # Try a more flexible approach - find and replace the function
    pattern = r'def is_sudan_relevant\(title, desc=""\):.*?return False'
    replacement = new
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
        print("Replaced via regex.")
    else:
        print("ERROR: Could not find pattern to replace.")
        exit(1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. fetch_news.py updated.")
print("Run: git add scripts/fetch_news.py && git commit -m 'Fix news filter: title-only matching' && git push")
