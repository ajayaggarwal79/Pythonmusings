hours=input("Enter hours")
try:
    hrs=float(hours)
Except:
    print("Error, Please enter numeric input")

Rate=input("Enter Rate")
try:
    rts=float(rate)
Except:
    print("Error, Please enter numeric input")
total=None
if (hrs >40):
    total=((hrs-40)*(rts*1.5))+(40*rts)
    print(total)
else:
    total=40*rts
    print(total) 
