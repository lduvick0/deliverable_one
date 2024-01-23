nameUser=input("Enter your name:")
numInput = int(input(nameUser+"Enter a number between 1 and 100: "))
if numInput%2!=0 and numInput<60:
    print(numInput,"is an odd number")