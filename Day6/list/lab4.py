#Write a Python program to get the smallest number from a list. 
numbers = [1,2,7,5,11,18,35,57,4]
lowest = min(numbers)
'''
b = len(numbers)-1
lowest = 0
for i in range(0,len(numbers)):
    a = 0
    for j in range(0,len(numbers)):
        if numbers[i]< numbers[j]:
            a =a+1
    if a == b:
        lowest = numbers[i]
'''
print(f"The Smallest Number in list is : {lowest}")

