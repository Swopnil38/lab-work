#Write a Python program to construct the following pattern, using a nested for loop.
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print(sep="\n")
k = 4
while True:
    for j in range(k):
        print("*",end=" ")
    print(sep="\n")
    k = k-1
    if k ==0:
        break
    

