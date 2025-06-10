def fun (n,d): 
    if n<=0: 
        return 
    else: 
        print(n) 
        n=fun(n-d,d) 
fun (100,7)