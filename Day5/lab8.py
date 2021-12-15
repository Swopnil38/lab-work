#write a program to get a fibonacci series between 0 to 50
a = 0
b = 1
print(a,end= ",")
print(b,end= ",")
while True:
    c = a+b
    a,b = b,c       #a = b  #b = c
    if c<=50:
        print(c,end = ",")
    else:
        break