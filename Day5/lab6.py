#Write a Python Program to count the number of even and odd numbers from a series of number.
num = [11,13,14,15,18,24,27,21]
odd,even = 0,0
for i in range(len(num)):
    w = num[i]
    if w%2 == 0:
        odd = odd + 1
    else:
        even = even + 1
print(f"The Total Number of Even are {even} and odd are {odd} ")