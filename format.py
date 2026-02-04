import re

name = input("Enter your name: ").strip()

# if "," in name:
#     last_name, first_name = name.split(", ?")
#     name = f"{first_name} {last_name}"
# print(f"Hello, {name}")

# matches = re.search(r"^(.+), *(.+)$", name)

# if matches:
#     name = matches.group(2) + " " + matches.group(1)

    # last_name = matches.groups(1)
    # first_name = matches.groups(2)
    # name = f"{first_name} {last_name}"

    # last_name, first_name = matches.groups()
    # name = f"{first_name} {last_name}"

if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}!")