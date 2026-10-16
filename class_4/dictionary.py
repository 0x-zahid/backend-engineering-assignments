# A dictionary stores data as key–value pairs. Instead of a numeric index, you look items up by a meaningful key

student = {
    "name": "Zahid",
    "age": 26,
    "department": "SWE",
    "cgpa": 3.5,
    "is_employee": True
}
print(f"{student["name"]}")

# Dictionaries are mutable: can be change value, add brand new key

student["age"] = 25 # change existing value
student["university"] = "Daffodil International University" # added new key

print(f"{student["university"]}")

# Dictionary Methods:
print(f"{student.keys()}")
print(f"{student.values()}")
print(f"{student.keys()}")
print(f"{student.get("is_employee")}")
print(f"{student.pop("is_employee")}")

print(f"{student.items()}")
print(f"{student.get("is_employee")}")

# Use .get() when a key might be missing; use [ ] when you're sure it exists.

# Nested Data the shape of real APIs
# Dictionaries can hold dictionaries, and lists can hold dictionaries. This is exactly how real
# backend data looks.

#In this example: Dictionaries can hold dictionaries s
user = {
    "id": "202-35-662",
    "name": "Zahid Hasan",
    "address": {
        "city": "Dhaka",
        "country": "Bangladesh"
    }
}

print(user["address"]["city"]) # Dhaka

user_x = [
    {"id": 202-35-662, "name": "Zahid Hasan", "age": 25},
    {"id": 202-35-662, "name": "Richard", "age": 26}
]

print(f"{user_x[0]["name"]}")
print(f"{user_x[1]["age"]}")


#and = both true.
# or = at least one true.
# not = flip True/False.
age = 25
salary = 50000
if age >= 18 and salary >= 30000:
    print("Eligible")
# and → both must be True
is_blocked = False
if not is_blocked:
    print("User can login")
print(f"{not is_blocked}")

# Real-world login check:
username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print(f"Login successful.")
else:
    print(f"Invalid username or password.")

# Nested If & Truthy / Falsy

has_ticket = True
age = 39
if age >= 18:
    if has_ticket:
        print(f"You can enter.")

if age >= 18 and has_ticket:
    print(f"You can enter.")

# Conditions + Data Structures
# Now combine everything. This is what real backend logic looks like.
numbers = [10, 20, 30 , 40]
if 30 in numbers:
    print(f"30 exists")

user = {
    "name": "Zahid",
    "age": 28,
    "employment_details": {
        "current_comapy":"Optimizely, Inc.",
        "role": "Software Engineer"
    }
}

if user.get("email"):
    print(f"{user["email"]}")
else:
    print(f"Email not found")



# print(f"{user.get("phone")}")
# print(user["name"])
# print(f"{user.get("year", "Not found, try again.")}")
# print(f"{user["employment_details"]["current_comapy"]}")
# # print(f"{user.get("role")}")

# print("role" in user["employment_details"])

