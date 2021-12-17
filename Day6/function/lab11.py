# Write a program to find the factorial of a number using functions
import math
def factorial(number):
    fact = math.factorial(number)
    return fact

num = int(input("Enter a Number to find it's Factorial: "))
print(f"The Factorial of {num} is : {factorial(num)}")