# set is a collection of unique values in curly braces. Duplicates are automatically dropped.

num = {1, 2, 2, 3, 3, 3}
print(f"{num}") #{1, 2, 3}

# There is a list, retrieve all unique element from the list:
input_list = [7, 7, 5, 4, 2, 9, 8]
unique_items = set(input_list)
print(f"{unique_items}") #{2, 4, 5, 7, 8, 9}

# retrieve all unique element from the list: and converting unique valus into list
unique_items_list = list(set(input_list))
print(f"{unique_items_list}")

# checking list or set:
if isinstance(unique_items, set):
    print(f"{unique_items} is a set")
if isinstance(unique_items_list, list):
    print(f"{unique_items_list} is a list")

#set operation:
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b) #union operation(everything)
print(a & b) #intersection(common)
print(a - b) #difference(in a, not b)
print(b - a) #difference(in b, not a)
print(a ^ b) #symmetric (not shared)


#1. Given two sets of student names, find the ones present in both (intersection).

name_set_1 = {"Zahid", "Richard", "Ronald", "Johnathan", "Kelly"}
name_set_2 = {"Richard", "Ronald", "Amenda", "Nick", "Huge", "Victor", "Zahid"}

print(f"Present in both name sets:{name_set_1 & name_set_2}")
