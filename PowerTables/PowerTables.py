confirmInput="y"
while confirmInput=="y":
    userInput = int(input("Enter an integer: "))
    print("{:<10} {:<10} {:<10}".format("Number", "Squared", "Cubed"))
    print("{:<10} {:<10} {:<10}".format("======","======","======"))
    #print(str(userInput)+"         "+str(userInput*userInput)+"         "+str(userInput**3))

    for i in range (1, userInput+1):
        print("{:<10} {:<10} {:<10}".format(i, i**2, i**3))
        #print(str(userInput-i)+"         "+str(((userInput-i)*(userInput-i)))+"         "+str((userInput-i)**3))

    print("\nMultiplication Table")
    print("{:<10} {:<10} {:<10} {:<10}".format(1,2,3,4))
    print("{:<10} {:<10} {:<10} {:<10}".format("=","=","=","="))
    for i in range (1, userInput+1):
        print("{:<10} {:<10} {:<10} {:<10}".format(i, i * 2, i * 3, i * 4))
    confirmInput = input("Do you want to continue? (y/n): ")