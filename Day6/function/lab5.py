'''
Write a function called show_stars(rows). If rowsis 5, it should print the following:
* 
**
***
****
***** 
'''
def show_stars(rows):
    for i in range(rows+1):
        for j in range(i):
            print("*",end = "")
        print("",sep = "\n")
row1 = int(input("Enter Number of rows: "))
show_stars(row1)