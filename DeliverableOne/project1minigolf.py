import math

holeone=0
holetwo=0
holethree=0
holefour=0
holefive=0
holesix=0
parcheck=0
person_name= input("Welcome to GC mini golf! What is your name? ")
num_holes= int(input("Hi " + person_name + "! Would you like to play 3 or 6 holes today?"))
if num_holes==6:
    holeone= int(input("How many putts for hole 1?(par is 3)"))
    holetwo= int(input("How many putts for hole 2? (par is 3)"))
    holethree= int(input("How many putts for hole 3? (par is 3)"))
    holefour= int(input("How many putts for hole 4? (par is 3)"))
    holefive= int(input("How many putts for hole 5? (par is 3)"))
    holesix= int(input("How many putts for hole 6? (par is 3)"))
    parcheck= holeone+holetwo+holethree+holefour+holefive+holesix
    totalscore= parcheck - 18
    if parcheck<=18:
        print(f"Great job {person_name}! Your total score was: " + str(totalscore))
    elif parcheck==18:
        print(f"Great job {person_name}! Your total score was: " + str(totalscore))
    else:
        print(f"Nice try {person_name}!Your total score was: " + str(totalscore))
elif num_holes==3:
    holeone = int(input("How many putts for hole 1?(par is 3)"))
    holetwo = int(input("How many putts for hole 2? (par is 3)"))
    holethree = int(input("How many putts for hole 3? (par is 3)"))
    parcheck = holeone + holetwo + holethree
    totalscore = parcheck - 9
    if parcheck <= 9:
        print(f"Great job {person_name}! Your total score was: " + str(totalscore))
    elif parcheck == 9:
        print(f"Great job {person_name}! Your total score was: " + str(totalscore))
    else:
        print(f"Nice try {person_name}!Your total score was: " + str(totalscore))
else:
    print("That is not a valid number, please choose either 3 or 6")