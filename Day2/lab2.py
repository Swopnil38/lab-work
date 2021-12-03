#find BMI of a person where take mass and height as input from the user
mass = int(input("Enter mass of a person(in kg): "))
height = int(input("Enter height of a person(in m): "))
BMI=mass/ (height)**2
print(f"The BMI of a person is {BMI}")
