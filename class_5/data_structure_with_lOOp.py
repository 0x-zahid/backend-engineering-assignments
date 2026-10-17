#tuple, set, dict, list

input_tuple = (1, 2, 3, 4, 5)
input_list = [1, 2, 3, 4, 5]
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
