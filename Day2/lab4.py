# N students take K apples and distribute them among each other evenly. The remaining
#(the indivisible) part remains in the basket. How many apples will each single student
#get? How many apples will remain in the basket? The program reads the numbers N and K. 

student = int(input("Enter the number of Students: "))
apple = int(input("Enter the Number of Apples: "))
distribute = apple//student
remaning = apple%student
print(f"Each student gets {distribute} No. of apples and {remaning} no. of apples are remaning")