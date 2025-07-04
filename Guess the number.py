import random

target = random.randint(1,100)

while True:
    Userchoice =input("Guess the target or Quit(Q) = ")
    if(Userchoice == "Q"):
        break

    Userchoice = int(Userchoice)

    if(Userchoice == target):
        print("You guessed it")
        break
    if(Userchoice < target):
        print("Your number was small")
    else:
        print("your number is too high")    

print("-----GameFininshed-----")    

