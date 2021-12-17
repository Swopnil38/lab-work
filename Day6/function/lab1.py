#Write a Python function to find the Max of three numbers 
def max(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(f"The greatest number is : {num1}")
    elif num2>num1 and num2>num3:
        print(f"The greatest number is : {num2}")
    elif num3>num1 and num3>num2:
        print(f"The greatest number is : {num3}")
    else:
        print("Error")

num11 = int(input("Enter any Number:"))
num12 = int(input("Enter any Number:"))
num13 = int(input("Enter any Number:"))

max(num11,num12,num13)