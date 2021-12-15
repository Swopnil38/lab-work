#Write a Python program that accepts a word from the user and reverse it.
word = input("Enter input a word: ")
i = len(word)
k = i+1
w = ""
for j in range(1,k):
    l = i-j
    w = w + word[l]
print(w)