#Write a Python program to convert temperatures to and from celsius, fahrenheit.
temp = input("Enter Temperature in Celcius or Fahrenite(C/F): ")
if temp == "C":
    temp1 = int(input("Enter Temperature in Celcius: "))
    fahr = ((temp1*9)/5)+32
    print(f"{temp1} in celcius is equal to {fahr} fahrenite")
elif temp == "F":
    temp2 = int(input("Enter Temperature in Fahrenite: "))
    C = (5/9) * (temp2 -32)
    print(f"{temp2} in Fahrenite is equal to {C} Celcius")
else:
    print("You entered Wrong value")  
