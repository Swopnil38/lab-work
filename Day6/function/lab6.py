#Write a Python program to reverse a string. 
word = input("Enter input a word: ")
def reverse(word1):
    w = ""
    for j in range(1,len(word1)+1):
        l = len(word1)-j
        w = w + word1[l]
    return w

rev = reverse(word)
print(f"The Reverse string of {word} is: {rev}")

        
        
