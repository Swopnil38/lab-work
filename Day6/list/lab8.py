#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
alpha = ["abcda","1478","1741","awca","fdk","aa","aq7u"]
alpha_new=[]
for i in range(0,len(alpha)):
    if i == 0 or i == 4 or i == 5:
        continue
    else:
        alpha_new.append(alpha[i])
print(alpha_new)