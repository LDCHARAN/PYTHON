#Tip, the waiter
def cal(bamt,tip_per):
    tot=bamt+bamt*tip_per*0.01
    tot=round(tot,2)
    print("Please pay",tot)

bill_amt=int(input("Enter bill amount : "))
tip_percentage=int(input("Enter tip percentage : "))
cal(bill_amt,tip_percentage)