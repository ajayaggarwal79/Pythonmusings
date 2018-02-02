hours=input("Enter hours")
hrs=float(hours)
Rate=input("Enter Rate")
rts=float(rate)
total=None
if (hrs >40):
    total=((hrs-40)*(rts*1.5))+(40*rts)
    print(total)
else:
    total=40*rts
    print(total) 

