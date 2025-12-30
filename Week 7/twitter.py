import re

url = input("URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

if match := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([A-Za-z0-9_]+)(?:/)?$", 
                      url, re.IGNORECASE):
    username = match.group(1)
    print(f"Username: {username}")