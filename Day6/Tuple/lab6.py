#Write a Python program to convert a tuple to a string. 
tup = ('s','w','o','p','n','i','l')
# using for loop
'''
stri = ""
for items in tup:
    stri = stri + items
'''
#using str.join
stri = "".join(tup)
print (stri)
print(type(stri))