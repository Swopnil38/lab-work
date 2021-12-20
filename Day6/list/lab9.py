#Write a Python program to select an item randomly from a list. 
import random
alpha = ["abcda","1478","1741","awca","fdk","aa","aq7u"]
a = random.randint(0,len(alpha))
print(f"The Randomly selected item  is: {alpha[a]}")