#Given a positive real number, print its fractional part. 
import math
num = float(input("Enter any Positive Real Number:"))
x,y = math.modf(num)
print(x)
print(y)
