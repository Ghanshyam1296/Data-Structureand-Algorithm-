# Try & Except block

while(True):
    try:
        userdata=input("enter a number: ")
        userdata=int(userdata)
    except ValueError:
        #print("Not a number.Please try again")
        pass
    else:
        break
