nameUser=input("Enter your name:")
validInput="n"
numInput=0
loopend= "y"
while loopend.lower() =="y":
    numInput = int(input(nameUser + " Enter a number between 1 and 100: "))
    while validInput != "y":
        if numInput < 1 or numInput > 100:

            print("Invalid Input please try again")
            numInput = int(input(nameUser + " Enter a number between 1 and 100: "))
        else:
            validInput = "y"
    if numInput%2 != 0 and numInput<60: #a
        print(str(numInput) +" Odd and less than 60")
    elif numInput % 2 == 0 and numInput >= 2 and numInput <= 24: #b
        print(str(numInput)+ " Even and less than 25")
    elif numInput % 2 == 0 and numInput>=26 and numInput <=60: #c
        print(str(numInput)+ " Even and between 26 and 60 inclusive.")
    elif numInput % 2 == 0 and numInput >60:#d
        print(str(numInput) + " Even and greater than 60")
    elif numInput % 2 != 0 and numInput >60:#e
        print(str(numInput) + " Odd and greater than 60")
    else:
        print("Invalid input")
    loopend = input("Would you like to continue (y/n): ")