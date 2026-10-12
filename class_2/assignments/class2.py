# input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
# input_list2 = [5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6]
# # Problem 1
# input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
# input_list1.append(10)
# print(f"After append: {input_list1}")
#
# input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
# input_list1.insert(0, 10)
# print(f"After insert: {input_list1}")
#
# input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
# input_list1.extend(input_list2)
# print(f"After extend: {input_list1}")
#
# input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
# input_list1.remove(2)
# print(f"After remove: {input_list1}")
#
# input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
# removed_item = input_list1.pop()
# print(f"Removed item: {removed_item}")
# print(f"After pop: {input_list1}")
#
# input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
# input_list1.sort()
# print(f"After sort: {input_list1}")
#
# input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
# input_list1.reverse()
# print(f"After reverse: {input_list1}")
#
# input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
# count = input_list1.count(2)
# print(f"2 appears {count} times")
#
# input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
# index = input_list1.index(3)
# print(f"Index of 3: {index}")
#
#
# # Problem 2
# numbers = list(map(int, input("Enter numbers: ").split()))
# if numbers == sorted(numbers):
#     print(f"The list is sorted")
# else:
#     print(f"The list is not sorted")
#
# # Problem 3
# numbers = [10, 20, 30, 40, 50]
# print(f"First 3 elements: {numbers[0:3]}")
# print(f"Middle elements: {numbers[1:4]}")
# print(f"Every 2nd element: {numbers[0:5:2]}")