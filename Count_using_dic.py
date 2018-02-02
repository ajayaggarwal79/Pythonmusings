fname=open("//gblonhome03/aggara1/Desktop/Python/mbox-short.txt")
email=dict()

for line in fname:
    line=line.strip()
    if '@' in line and line.startswith ('From:'):
        a,b=line.split()
        email[b]=email.get(b,0)+1
lst=list()
for k,v in list(email.items()):
    lst.append((v,k))
lst.sort(reverse=True)

for k,v in lst[:1]:
    print(v,k)

    
