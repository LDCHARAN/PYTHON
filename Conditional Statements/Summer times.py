#write a program to check whether you are Qualified for the next round or not.(A person will be Qualified for the next round only hehis point are more than 100)
P=int(input("Enter your points : "))
if P>100:
    print("Great!You are qualified for the next round...")
else:
    print("You are not qualified for the next round.Better luck next time!")

#Write a program to check whether the year is leap year or not
Y=int(input("Enter the year : "))
if Y%4==0:
    print(Y,"is a leap year")
else:
    print(Y,"is not a leap year")