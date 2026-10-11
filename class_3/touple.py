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

print(input_tuple[1])
print(input_tuple[::-1])
print(input_tuple[-1])

# Real Life uses:
designation = ("Software Engineer", "Data Scientist", "Data Analyst")

for i in designation:
    designation[0] = "Software Developer"
# TypeError: 'tuple' object does not support item assignment
