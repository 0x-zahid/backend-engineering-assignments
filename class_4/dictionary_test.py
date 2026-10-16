input_dict = {
    "name": "Zahid",
    "age": 20,
    "id": "202-35-662",
    "my_identity": {
    "nid": 1231,
    "phone": "015",
    "email": "droptozahid@gmail.com"
}
}
phone_number = input_dict["my_identity"]["phone"]
print(f"{phone_number}")

person_email = input_dict.get("my_identity").get("email")
print(f"{person_email}")
# Interview common qus: .get() and [] when to use ...
print(input_dict["name"])
print(input_dict.get("email"))

print(input_dict.keys())
print(input_dict.values())
print(input_dict.items())

input_dict.pop("age")
print(input_dict)