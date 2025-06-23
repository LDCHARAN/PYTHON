#Get rid of duplicates
s={'1':{'Name':'Durga Charan','Age':13},'2':{'Name':'Pranav','Age':12},'3':{'Name':'Priyank','Age':12},'4':{'Name':'Durga Charan','Age':13}}
res={}
for k,v in s.items():
    if v not in res.values():
        res[k]=v
print(res)