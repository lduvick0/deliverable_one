import math

numapple=0
numorange=0
numgrape=0
subtotal=0
continueloop=0
taxtotal=0.05
totalprice=0
userinput=" "
print("Welcome to the GC Fruit Market!")
personname=input("What is your name?\n")

#I know I could've done a list for the fruit table but this is how my brain works
while continueloop==0:
    fruitchoice=input("Welcome "+personname+ "! Which fruit would you like to buy\n 1. Apple $2\n 2. Grape $1\n 3. Orange $3\n")
    if fruitchoice=="1":
        print("You bought 1 apple at $2")
        numapple+=1
        subtotal+=2
        userinput=input("Would you like to buy another piece of fruit? y/n\n")
        if userinput=="y":
            continueloop=0
        elif userinput=="n":
            continueloop=1
        else:
            print("Invalid input please try again")
    elif fruitchoice=="2":
        print("You bought 1 grape at $1")
        numgrape+=1
        subtotal+=1
        userinput=input("Would you like to buy another piece of fruit? y/n\n")
        if userinput=="y":
            continueloop=0
        elif userinput=="n":
            continueloop=1
        else:
            print("Invalid input please try again")
    elif fruitchoice=="3":
        print("You bought 1 orange at $3") #crazy prices for oranges nowadays
        numorange+=1
        subtotal+=3
        userinput= input("Would you like to buy another piece of fruit? y/n \n")
        if userinput=="y":
            continueloop=0
        elif userinput=="n":
            continueloop=1
        else:
            print("Invalid input please try again")
    else:
        print("Invalid input please try again")

print("Order for "+personname)
print(str(numapple)+ "apple(s) at $2 apiece")
print(str(numgrape)+ "grape(s) at $1 apiece")
print(str(numorange)+ "orange(s) at $3 apiece")
taxtotal*=subtotal
totalprice=subtotal+taxtotal
print("Sub Total: $"+str(subtotal))
print("5% Tax: $"+str(taxtotal))
print("Total: $"+str(totalprice))

