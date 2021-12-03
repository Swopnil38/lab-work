'''
A school decided to replace the desks in three classrooms. Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks
that can be purchased.
'''
classroom1 = int(input("Enter No. of Students in classroom 1: "))
classroom2 = int(input("Enter No. of Students in classroom 2: "))
classroom3 = int(input("Enter No. of Students in classroom 3: "))

desk1 = classroom1//2
if classroom1%2 != 0:
    desk1 = desk1+1
desk2 = classroom2//2
if classroom2%2 != 0:
    desk2 = desk2+1
desk3 = classroom3//2
if classroom3%2 != 0:
    desk3 = desk3+1
    
required_desk = desk1 + desk2 + desk3
print(f"The total No. of required Desk is: {required_desk}")

