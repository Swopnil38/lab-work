#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
def check_case(string1):
    j,k = 0,0
    for l in range(len(string1)):
        i = string1[l]
        if i.isupper():
            j +=1
        else:
            k += 1
    return j,k



word = input("Enter input a word: ")
Upper_coint,Lower_count = check_case(word)
print(f"The total upper case is {Upper_coint} and lower case is {Lower_count}")