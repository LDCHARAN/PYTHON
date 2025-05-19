h=float(input("Enter your height in cm : "))
w=float(input("Enter your weight in kg : "))
BMI=w/(h/100)**2
print(("Your BMI is ",BMI))
if BMI <=18.4:
    print("You are under weight")
elif BMI <=24.9:
    print("You are healthy")
elif BMI <=29.9:
    print("You are over weight")
elif BMI <=34.9:
    print("You are severely overweight")
elif BMI <=39.9:
    print("You are obese")
else:
    print("you are severely obese")