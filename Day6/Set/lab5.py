#Write a Python program to remove an item from a set if it is present in the set.  
integers = {1,2,3,4,5}
for item in integers:
    if item == 6:
        integers.remove(6)
    else:
        continue
print(integers)
