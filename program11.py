# Task 11: Add 1 to each item in a list of first 10 even numbers
even_numbers = list(range(2, 21, 2))
updated_numbers = []

for num in even_numbers:
    updated_numbers.append(num + 1)

print("Updated even numbers:", updated_numbers)
