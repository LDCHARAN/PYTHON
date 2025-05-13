amount=int(input("Enter Amount:"))
n2000=amount//2000
amount=amount%2000
n500=amount//500
amount=amount%500
n100=amount//100
amount=amount%100
n10=amount//10
amount=amount%10
n1=amount//1
print("your entered amount",amount,"contains : ")
print("total 2000notes:",n2000)
print("total 500 notes :",n2000)
print("total 100 notes :",n2000)
print("total 10 notes :",n10)
print("total 1 notes :",n1)