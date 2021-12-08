#Write a Python program to sum three given integers. However, if two or more values are
#equal sum will be zero.
num1 = int(input("Enter a Number:"))
num2 = int(input("Enter a Number:"))
num3 = int(input("Enter a Number:"))
if (num1 != num2 and  num2 != num3 and num3 != num1):
    sum = num1 + num2 + num3
    print (f"The sum of 3 Integer {num1},{num2} & {num3} is: {sum}")
    
else:
    print("Two or more than Two Number are same.")