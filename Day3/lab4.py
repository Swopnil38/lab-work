#Given three integers, print the smallest one. (Three integers should be user input) 
num1 = int(input("Enter first Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
if (num1<num2) and (num1<num3):
    print(f"The smallest Number is: {num1}")
elif (num1>num2) and (num2<num3):
    print(f"The smallest number is: {num2}")
else:
    print(f"The smallest number is: {num3}")
    
     