# Write a Python program to swap two variables.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# swap two numbers
print(f"original numbers are num1 = {num1} and num2 = {num2}")
tmp = num1
num1 = num2
num2 = tmp
print(f"original numbers are num1 = {num1} and num2 = {num2}")
