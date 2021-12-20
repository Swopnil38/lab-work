#Write a Python program to get the largest number from a list.

numbers = [1,2,7,5,11,18,35,57,4]
great = max(numbers)
'''
b = len(numbers)-1
great = 0
for i in range(0,len(numbers)):
    a = 0
    for j in range(0,len(numbers)):
        if numbers[i]> numbers[j]:
            a =a+1
    if a == b:
        great = numbers[i]
'''      
print(f"The Largest Number in list is : {great}")

