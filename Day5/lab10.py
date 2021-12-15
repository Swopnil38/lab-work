#write a Python Program that accepts a string and calculate number of digits and letters
'''
word = input("Enter a string: ")
letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
number = [0,1,2,3,4,5,6,7,8,9]
space= [" "]
letter_count,space_count,number_count = 0,0,0
for i in range(len(word)):
    q = word[i]
    a = 0
    while True:
        if q == letter[a] or q == (letter[a].upper()):
            letter_count = letter_count + 1
        if a<10:
            if q == str(number[a]):
                number_count = number_count + 1
        if a<1:
            if q == space[a]:
                space_count = space_count +1
        a = a+1
        if a>25:
            break
total_count = letter_count + number_count + space_count
special_count = len(word) - total_count
print(f"The toal letter,number,spaces,special character in the string ( {word} ) is :  {letter_count},{number_count},{space_count} & {special_count} respectively.")
'''
word = input("Enter a string: ")
letter_count,space_count,number_count = 0,0,0
for character in word:
    if character.isalpha():
        letter_count = letter_count + 1
    if character.isnumeric():
        number_count = number_count + 1
    if character.isspace():
        space_count = space_count + 1
total_count = letter_count + number_count + space_count
special_count = len(word) - total_count
print(f"The toal letter,number,spaces,special character in the string ( {word} ) is :  {letter_count},{number_count},{space_count} & {special_count} respectively.")
    



