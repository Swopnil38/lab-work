# Write a Python program to sum all the items in a list. 

numbers = [1,2,7,5,11,18,35,57]

sum_total = sum(numbers)
'''
sum_total = 0
for i in range(len(numbers)):
    sum_total = sum_total + numbers[i]
'''

print(f"The Sum of all Item in list is : {sum_total}")
