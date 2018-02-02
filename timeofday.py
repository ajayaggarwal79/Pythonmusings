fname=open("//gblonhome03/aggara1/Desktop/Python/mbox-short.txt")
hours=dict()
#hours=None

for line in fname:
    line=line.strip()
    #print(line)
    if line.startswith('From') and len(line.split())>2 :
        a,b,c,d,e,f,g=line.split()
        h,i,j=f.split(':')
        #print(h)
        hours[h]=hours.get(h,0)+1
lst=list()
for key, val in list(hours.items()):
    lst.append((key,val))
lst.sort()
for key, val in lst[:]:
    print(key, val)
#print(hours)

