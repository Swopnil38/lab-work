#WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
subject1 = int(input("Enter marks in First Subject: "))
subject2 = int(input("Enter marks in Second Subject: "))
subject3 = int(input("Enter marks in Third Subject: "))
subject4 = int(input("Enter marks in Four Subject: "))
total_mark = subject1 + subject2 + subject3 + subject4
print(f"The Total marks you scored is {total_mark}")
percentage = (total_mark/400)*100
print(f"You scored {percentage}%")
if percentage>70 :
    print("You scored Distinction.")
elif percentage>60:
    print("YOu scored First Grade.")
elif percentage>40:
    print("You Passed.")
else:
    print("You Failed.")        