# Write a Python program to do arithmetical operations addition and division.
num1 = int(input("enter number1:"))
num2 = int(input("enter number2: "))
sum_result = num1+num2
print(f"sum:{num1}+{num2}={sum_result}")

#division of two numbers
num3 = int(input("enter dividend number:"))
num4 = int(input("enter divisor number: "))

if num4 == 0:
    print("number cannot be divided by zero")
else:
    result = num3/num4
    print(f"Division:{num3}/{num4}={result}")