#Accept string from the user and display only those characters which are present at an even index 
def reverse(word1):
    w = ""
    for i in range(1,len(word1)):
        if i%2 != 0:
            w = w + word1[i]
    return w

word = input("Enter a string to print even characters: ")
print(f"The character on even index is {reverse(word)}")