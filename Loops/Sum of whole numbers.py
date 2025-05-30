#Write a program to calculate the sum of whole numbers
N=int(input("Enter n"))
sum=0
for x in range(1,N+1):
    sum=sum+x
print("Summation of",N,"whole numbers = ",sum)