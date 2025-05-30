#Write a program to reverse the string entered by the user.
S=input("Enter a string : ")
rs=""
for ch in S:
    rs=ch+rs
print("Reverse string of",S,"is :",rs)