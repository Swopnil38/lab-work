#write a Python program to find a factorial of a number
import math
num = int(input("Enter any Number to find it's factorial:"))
'''
num1 = num
factorial = 1
while True:
    factorial = factorial * num
    num = num - 1
    if num == 0:
        break
print(f"The factorial of {num1} is : {factorial}")
'''
factorial = math.factorial(num)
print(f"The factorial of {num} is : {factorial}")