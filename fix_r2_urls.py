import re

OLD = "pub-0c3bb637d5f54b239fe4a4ef9b08bfe3.r2.dev"
NEW = "pub-a5e3b47fe87749f491660d68e2029284.r2.dev"

import os
base = os.path.dirname(os.path.abspath(__file__))

# Fix library.json
json_path = os.path.join(base, "data", "library.json")
with open(json_path, encoding="utf-8") as f:
    content = f.read()
count = content.count(OLD)
fixed = content.replace(OLD, NEW)
with open(json_path, "w", encoding="utf-8") as f:
    f.write(fixed)
print("library.json: replaced " + str(count) + " URLs")

# Fix library_inventory.csv
csv_path = os.path.join(base, "library_inventory.csv")
with open(csv_path, encoding="utf-8") as f:
    content = f.read()
count2 = content.count(OLD)
fixed2 = content.replace(OLD, NEW)
with open(csv_path, "w", encoding="utf-8") as f:
    f.write(fixed2)
print("library_inventory.csv: replaced " + str(count2) + " URLs")

print("\nDone. All R2 URLs now point to pub-a5e3b47fe87749f491660d68e2029284.r2.dev")
