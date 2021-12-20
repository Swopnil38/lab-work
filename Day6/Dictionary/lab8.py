#Write a Python script to merge two Python dictionaries. 
int1 = {"first":1,"second":2}
int2 = {"third":3,"fourth":4}
int3 = int1.copy()
int3.update(int2)
print(int3)