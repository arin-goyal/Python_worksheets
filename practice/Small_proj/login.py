import numpy

uname = "Arin Goyal"
passw = "Hello123"
no= 6377016294

# print("1. Login")
# print("2. Exit")




# option1 = int(input("\nChoose option - "))
while True :
    print("\n1. Login")
    print("2. Exit")
    option1 = int(input("\nChoose option - "))
    if option1 == 1:
        username = str(input("\nEnter username - "))
        password = str(input("Enter your password - "))
        
        if username == uname and password == passw:
            print("Login succesfull...")
            exit()

        elif username != uname or password != passw:
            print("\nWrong Username or Password entered !")
            print("\n1.Enter details again")
            print("2.Forgot password")
            print("3.Exit")

            option2 = int(input("\nChoose option - "))
            if option2 == 2:
                
                while True:
                    print("1.Login by phone no.")
                    print("2.Exit")
                    option3 = int(input("Choose option 3 - "))
                    if option3 == 1:
                        number=str(input("Enter your mobile no."))
                        if number==no:
                            print("OTP sent")
                        else:
                            print("Either wrong number or account does not exist")
                            continue
                    
                break
            elif option2 == 3:
                break




    elif option1 == 2:
        exit()

    else :
        print("Wrong input try again")
        continue
    
