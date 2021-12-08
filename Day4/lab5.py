'''
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
'''
total_classes = int(input("Total Number of classes held:"))
attend_classes = int(input("Total Number of Classes Attended:"))
percent_class_attend = (attend_classes/total_classes)*100
print(f"Student attended {percent_class_attend}% of classes.")
if percent_class_attend<75:
    print(f"Sorry,You aren't allowed to sit in exam.")
else:
    print(f"Congratulations! You are allowed to sit in exam.")