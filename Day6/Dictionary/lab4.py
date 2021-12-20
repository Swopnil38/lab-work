#Write a Python script to check if a given key already exists in a dictionary.  
a = input("Enter a key to remove from Dictionary if it is present: ")
integer = {"first":1,"third":3,"fifth": 5,"second":2,"ninty":90}
for items in integer:
    if str(items) == a:
        integer.pop(a)
print(integer)
