#Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.
M=input("Any medical cause ? (yes/no)")
if M.lower()=='yes':
    C=input("Do you have medical certificate ? (yes/no)")
    if C.lower()=='yes':
        print("You can appear for the exam")
    else:
        print("You can not appear for the exam")
else:
    A=int(input("Enter student's attendence percentage : "))
    if A>75:
        print("You can appear for the exam")
    else:
        print("You can not appear for the exam")