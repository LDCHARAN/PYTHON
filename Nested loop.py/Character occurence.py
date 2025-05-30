#Write a program to check how many times a character is repeated in a word? 
while True: 
    w=input("Enter your word: ") 
    ch=input("Enter the character: ")
    c=0  
    for x in w:
        if x==ch:
            c+=1
        print("Character", ch, "is present", c, "number of times in",w) 
        choice=input("Do you want to continue? (y/n)") 
        if choice not in('y', 'Y'): 
            break