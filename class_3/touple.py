# input_touple = (1, 2, 3, 4, 5, 0)

# print(f"length of the touple:{len(input_touple)}")
# print(f"Last Item: {input_touple[len(input_touple)-1]}")
# last_item = input_touple[-1]
# print(f"{last_item}")

# input_touple.add(6) touple is immutable
# input_touple[0] = 10

# original = (10, 20, 30, 40)
# sliced = original[1:3]  # Returns (20, 30)
# print(id(original))
# print(id(sliced))
# print(id(original) == id(sliced))  # Output: False (Different memory addresses)
# print(original is sliced)          # Output: False

# original = (10, 20, 30, 40)
# full_sliced = original[:]  # Returns (10, 20, 30, 40)

# print(id(original) == id(full_sliced))  # Output: True (Same memory address!)
# print(original is full_sliced)          # Output: True

# original = (10, 20, 30, 40)
# sliced = original[1:3]  # Returns (20, 30)

# print(id(original) == id(sliced))  # Output: False (Different memory addresses)
# print(original is sliced)          # Output: False

input_tuple = (1, 2, 3, 4, 5)
full_sliced = input_tuple[:]
print(input_tuple[-2])
print(input_tuple[::-1])
print(input_tuple[1:3])
print(input_tuple[-1])


# Real Life uses:
eiffel_tower_location = (48.8584, 2.2945)

# 2. Access the data using indexing
latitude = eiffel_tower_location[0]
longitude = eiffel_tower_location[1]

print(f"The Eiffel Tower is located at Latitude: {latitude} and Longitude: {longitude}")

# another example:
designation = ("Software Engineer", "Data Scientist", "Data Analyst")

for i in designation:
    designation[0] = "Software Developer"
# TypeError: 'tuple' object does not support item assignment
