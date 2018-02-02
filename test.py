def computepay(h,r):
    total=0
    if(h>40):
        total=(h-40)*(rate*0.5)+(h*rate)
        return(total)
    else:
        total=h*rate
        return(total)

hrs=input("Enter Hours:")
h=float(hrs)
rt=input("Enter Rate")
rate=float(rt)
p = computepay(h,rate)
print("Pay",p)