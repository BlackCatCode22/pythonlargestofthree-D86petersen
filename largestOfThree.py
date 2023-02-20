# largestOfThree.py
# Dustin Petersen
# 2/19/2023
#
#
print("================================ Greatest of three numbers program ================================")

# getting user input and casting it to integer
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

# Getting the sum of the 3 numbers and assigning to variable total.
total = num1 + num2 + num3

# Assigning num1 as the largest number by default
largest = num1

# Comparing numbers using if else logic statements to see which is the largest of the 3 numbers
if num2 > largest:
    largest = num2

if num3 > largest:
    largest = num3

# Printing the output back to the user
print(f"The largest of the 3 numbers is {largest}")
print(f"The sum of the 3 numbers is {total}")
