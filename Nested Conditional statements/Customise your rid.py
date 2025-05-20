#Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options
R=input("Enter the ride which you prefer(bike/car) : ")
if R.lower()=='car':
    C=input("Which car do you prefer(sedan/SUV/Mini) : ")
    if C.lower()=='sedan':
        print("Your sedan ride's fare will be Rs.40 per hour.")
    elif C.lower()=='suv':
        print("Your suv ride's fare will be Rs.45 per hour.")
    else:
        print("Your mini ride's fare will be Rs.50 per hour.")
else:
    C2=input("Which car do you prefer(Cruiser,Bobber,Bagger) : ")
    if C2.lower()=='cruiser':
        print("Your cruiser's ride fare will be Rs.20 per hour.")
    elif C2.lower()=='bobber':
        print("Your bobber's ride fare will be Rs.25 per hour.")
    else:
        print("Your Bagger's ride fare will be Rs.30 per hour.")