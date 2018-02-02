import re
#str1=input("Enter expression type")

fname=open("//gblonhome03/aggara1/Desktop/Python/regex_sum_60172.txt")
count=0

for line in fname:
    line=line.strip()
    x=re.findall('[0-9]+',line)
    if len(x)>0:
        for a in x:
            a=int(a)
            count=count+a
print(count)

        
        

    
