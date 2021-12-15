#Write a Python program to guess a number between 1 to 9.
import random
target_num, guess_num = random.randint(1,10),0
while target_num != guess_num:
    guess_num = int(input("Guess Number until you get it right: "))
print(f"Congrats! You guessed the correct number {target_num}")