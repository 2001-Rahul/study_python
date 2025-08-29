import random
choosen=random.randint(1,100)
nguess=0
userguess=None
while userguess!=choosen:
    userguess=int(input('enter your guess '))
    nguess+=1
    
    if userguess==choosen:
        print(f"you won correct guess...number of guess={nguess}")
    else:
        if userguess<choosen:
            print ("enter a larger number")
        else:
            print("enter a smaller number")        

with open("highscore.txt") as f:
    guessfile=int(f.read())
    if guessfile>nguess:
        with open("highscore.txt","w")as f:
            f.write(str(nguess))