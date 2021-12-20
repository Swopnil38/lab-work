#Write a Python script to concatenate following dictionaries to create a new one. 
int1 = {"first":1,"second":2}
int2 = {"third":3,"fourth":4}
int3 = {}
for i in (int1,int2):
    int3.update(i)
print(int3)