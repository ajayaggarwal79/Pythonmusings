import re
str1=input("Enter expression type")

fname=open("//gblonhome03/aggara1/Desktop/Python/mbox.txt")
count=0

for line in fname:
    line=line.strip()
    x=re.findall(str(str1),line)
    if len(x)>0:
        count=count+1
print(str(fname) +" " + "had " + str(count) +" lines that matched " +str1)
        
        

    
