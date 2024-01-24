actual_temp= 0
desired_temp= 0
def heating_cooling(actual_temp,desired_temp):
    continueConf = "y"
    while continueConf=="y":
        actual_temp = int(input("Enter the current room temperature: "))
        desired_temp = int(input("Enter the desired room temperature: "))
        if actual_temp<desired_temp:
            print("Run Heat")
        elif actual_temp>desired_temp:
            print("Run A/C")
        elif actual_temp==desired_temp:
            print("Standby")
        continueConf=input("Do you want to change the temperature again? (y/n)")


heating_cooling(actual_temp,desired_temp)