import re
email = input("Enter your email: ").strip()

# if "@" and "." in email:
#     print("Valid Email")
# else:
#     print("Invalid Email")

username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid email")
# else:
#     print("Invalid email")

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
if re.search(r"^(\w|\s)+@(\w+\.)?\w+\.(com|edu|gov|org|net)$", email, re.IGNORECASE): # \w = [a-zA-Z0-9_]
# if re.search(r".{1}.*@.*", email):
    print("Valid email")
else:
    print("Invalid email")