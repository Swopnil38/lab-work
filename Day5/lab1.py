#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
a = range(1500,2701)
i = 1500
while i in a :
    div7 = i%7
    div5 = i%5
    if div7==0 and div5==0 :
        print (i)
    i = i+1

    