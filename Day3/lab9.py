#Take username and password from user and check it again for the three times whether the user has entered the right
#username and password. If yes then print a message "Logged in Successfully", if not then print invalid credentials
#for consecutive 3 times and if the limit exceeds than print "Attempt finished".
for i in range(3):
    username = input("Enter Your Username: ")
    password = int(input("Enter Your Password: "))
    
    if (password == 123) and (username == "swopnil"):
        print("Logged in Successful")
        break
    else:
        print("Invalid Credentials")
else:
    print("Attempt Finished.")