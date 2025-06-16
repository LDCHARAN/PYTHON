#Rock Paper scissors
import random as rd
points=0
while True:
    uchoice=input("Enter your choice from [Rock(R) Paper(P) Scissors(S)]")
    L=['R','P','S']
    cchoice=rd.choice(L)
    print("Upi chose ",uchoice,"and computer chose",cchoice)
    if uchoice==cchoice:
        print("It is a tie")
    elif uchoice=='R':
        if cchoice=='S':
            print("You win")
            points+=1
        else:
            print("You lose")
            points-=1
    elif uchoice=='P':
        if cchoice=='R':
            print("You win")
            points+=1
        else:
            print("You lose")
            points-=1
    elif uchoice=='S':
        if cchoice=='P':
            print("You win")
            points+=1
        else:
            print("You lose")
            points-=1
    x=input("Do you want to continue (y/n)?")
    if x=='n' or x=='N':
        print("Your score is : ",points)
        break