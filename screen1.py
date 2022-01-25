print("Number Guessing Game")
import random
N=random.randint(1,9)

i=0
while i<5:
    Guess=int(input("Enter Your Guess"))
    if Guess == N:
        print("CONGRATS YOU WON!!")
    elif Guess<N :
        print("Your Number Is Less Plz Select A Higher Number Then",Guess)
    else:
        print("Your Number Is High Plz Select A Lesser Number Then",Guess)
    
    i=i+1

if i >=5:
    print("YOU LOSE,Your Number Is",N)    
