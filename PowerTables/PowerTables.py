userInput = int(input("Enter an integer: "))

print("{:<10} {:<10} {:<10}".format("Number", "Squared", "Cubed"))
print("{:<10} {:<10} {:<10}".format("======","======","======"))
#print(str(userInput)+"         "+str(userInput*userInput)+"         "+str(userInput**3))

for i in range (1, userInput+1):
    print("{:<10} {:<10} {:<10}".format(i, i**2, i**3))
    #print(str(userInput-i)+"         "+str(((userInput-i)*(userInput-i)))+"         "+str((userInput-i)**3))