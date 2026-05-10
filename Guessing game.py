# Guessing-game
my third project 



import random 

number = random.randint(0,100000000000)           #randint mean random no. between n1 and n2


while True:


    guess = int(input("Guess the number :"))

    if guess == number :
        print ("Correct")
        break


    elif guess > number:
        print("Too High")

        if guess > number:
            print("Dont be so sad")

    else :
        print("Too Low")
