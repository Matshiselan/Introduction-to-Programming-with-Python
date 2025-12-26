import re

email = input("Enter your email address: ")
# username, dormain = email.split("@")

# if (username) and dormain.endswith(".edu"):
#     print("Valid email")
# else:
#     print("Invalid email")

# if re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.edu$", email):
#     print("Valid email")
# else:
#     print("Invalid email")

if re.search(r'^(\w+|\D+|\S+)+@(\w+\.)?\w+\.(edu|com|edu|gmail)$', 
             email, re.IGNORECASE):
    print("Valid email")
else:
    print("Invalid email")