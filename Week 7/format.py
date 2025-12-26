import re

name = input("Name: ").strip()
if matches := re.search(r'^(.+), *(.+)$', name):
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"Hello, {name}")