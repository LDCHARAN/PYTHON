import random as rd
import time
def fl(sd,ed):
    print("Printing random date between ",sd,"and",ed)
    r=rd.random()
    dformat="%m/%d/%y"
    stime=time.mktime(time.strptime(sd,dformat))
    etime=time.mktime(time.strptime(ed,dformat))
    rtime=stime+r*(etime-stime)
    rdate=time.strftime(dformat,time.localtime(rtime))
    return rdate
d1=input("Enter first date : ")
d2=input("Enter second date : ")
print("Random date = ",fl(d1,d2))