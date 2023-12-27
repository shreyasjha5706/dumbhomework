# Task 20: Find the sum of all numbers stored in a list using a for loop in the list declaration
input_numbers = input("Enter numbers separated by space: ")
numbers_list = []

for x in input_numbers.split():
    numbers_list.append(int(x))

sum_of_numbers = sum(numbers_list)

print("Sum of numbers in the list:", sum_of_numbers)
