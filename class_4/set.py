# set is a collection of unique values in curly braces. Duplicates are automatically dropped.

num = {1, 2, 2, 3, 3, 3}
print(f"{num}") #{1, 2, 3}

# There is a list, retrieve all unique element from the list:
input_list = [1, 2, 3, 3, 4, 5, 6, 6, 7]
unique_items = set(input_list)
print(f"{unique_items}")