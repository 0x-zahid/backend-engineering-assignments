# tuple, set, dict, list

input_tuple = (1, 2, 3, 4, 5)
input_list = [1, 2, 3, 4, 5]

# check (from the list) whether 4 exist or not:
is_exist_4 = False
for item in input_tuple:
    if item == 4:
        is_exist_4 = True
        break
if is_exist_4 == True:
    print(f"4 is exist")
else:
    print(f"4 is not exist")

# print(input_dict.items())

# input_dict = {
#     "name": "Zahid",
#     "age": 20,
#     "id": "202-35-662",
#     "my_identity": { "nid": 1231, "phone": "015", "email": "droptozahid@gmail.com" },
#     "gadget_list": ["2 laptop", "1 camera", "2 smartphone", "3 smartwatch"]
# }
# for key, value in input_dict.items():
#     if type(value) is dict:
#         for key2, value2 in value.items():
#             print(f"    {key2}: {value2}")
#             # print(f"{value}")
#     elif type(value) is list:
#         for item in value:
#             print(f"{item}")
#     print(f"{key}: {value}")
    # print(type(value))


input_dict = {
    "name": "Zahid",
    "age": 20,
    "id": "202-35-662",
    "my_identity": {
        "nid": 1231,
        "phone": "015",
        "email": "droptozahid@gmail.com"
    },
    "gadget_list": [
        "2 laptop",
        "1 camera",
        "2 smartphone",
        "3 smartwatch"
    ]
}

for key, value in input_dict.items():
    # print(f"{key}: {value}")
    if type(value) is dict:
        for key2, value2 in value.items():
            print(f"  {key2}: {value2}")

    elif type(value) is list:
        for item in value:
            print(f"  {item}")
    else:
        print(f"{key}: {value}")
