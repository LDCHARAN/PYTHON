#Number game
import random as rd
x=True
n=str(rd.randint(10,20))
print("I will generate a number  from 10 to 20 and you have to guess that number")
print("The game ends when you get 1 hero!")
c=0
while x:
    c+=1
    g=input("Give me your best guess : ")
    if n==g:
        print("You win the game in",c,"attempts")
        print("The number was ",n)
        break
    else:
        print("Your guess is not correct.....try again \n\n")