count=0
total=0

while True:
    line=input('Enter number')
    if line=='done':
        break
    try:
        x=float(line)
        count=count+1
        total=total+x
        print('Enter a number', x)
        print(total, count, total/count)
    except:
        print('Enter a number:','bad data')
        continue
        
    
    



