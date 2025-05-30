#Write a program to demonstrate a Floyd triangle pattern?
r=int(input("Enter number of rows : "))
c=1
for i in range(1,r+1):
    for j in range(1,i+1):
        print(c,end=" ")
        c=c+1
    print()