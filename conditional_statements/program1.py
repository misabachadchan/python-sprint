#write a program to find greatest of 4 numbers entered by user

# Input four numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
# Find the greatest number
greatest = num1  # Assume num1 is greatest initially
if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
if num4 > greatest:
    greatest = num4
# Print the greatest number
print("The greatest number is:", greatest)