import re

url = input("Enter url: ").strip()
print(f"Twitter URL: {url}")

# username = url.replace("https://twitter.com/", "")
# username = url.removeprefix("https://twitter.com/")

# matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
# if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
if matches := re.search(r"^https?://(?:www\.)?twitter\.(?:com|org)/(.+)$", url, re.IGNORECASE):
    print(f"Twitter Username: {matches.group(1)}")