#Diamond Pattern
r=int(input("Enter number of rows : "))
if r%2==0:
    m=r//2
else:
    m=r//2+1
s=m-1
for i in range(1,m+1):
    for k in range(1,s+1):
        num=1
        s=s-1
        print()
        for j in range(1,2*i):
            print(num,end="")
            num=num+1
        print()
s=1
for i in range(1,m+1):
    for k in range(1,s+1):
        num=1
        s=s-1
        print(" ",end="")
        for j in range(1,2*i):
            print(num,end="")
            num=num+1
        print()