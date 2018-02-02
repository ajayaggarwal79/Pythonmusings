import re


fname=open("//gblonhome03/aggara1/Desktop/Python/mbox-short.txt")
count=0
pattern="New Revision"
pattern=pattern+"\S"
for line in fname:
    line=line.strip()
    x=re.findall(pattern,line)
    #print(x)
    if len(x)>0:
        print(x)
        count=count+1
#print(str(count) +" lines that matched ")
