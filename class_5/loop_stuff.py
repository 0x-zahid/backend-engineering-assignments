# Example of for loop:
num = int(input("Enter a number:"))
for i in range(0, num):
    print(f"value of i is: {i}")

print("------------------------")
n = 0
while n < num:
    print(f"value of n is: {n}")
    n += 1

input_list = [3, 2, 1, 5, 6]
# len_of_Input_list = len(input_list)
for item in range(0,len(input_list)):
    print(f"{input_list[item]}")


# another way:
another_list = [10, 20, 30, 40, 50]
for item in another_list:
    print(f"{item}")


# while loop

new_list = [3, 2, 1, 5, 6]
i = 0
while i < len(new_list):
    print(f"{new_list[i]}")
    i += 1

