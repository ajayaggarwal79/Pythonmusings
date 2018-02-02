"""
Differences   
""" 
def singleline_diff(line1, line2):
    """
    function to return the point  
    or index when the string changes
    """
    len_s1=len(line1)
    len_s2=len(line2)
    len_s3=min(len_s1,len_s2)
    #print(s3)
    count=0
   # x=None
    if len_s1==0 and len_s2==0:
        return -1
    elif len_s1==0 or len_s2==0:
        return min(len_s1,len_s2)
    
    while True and count<len_s3:
        if line1==line2:
            return -1        
        elif len_s1<len_s2 and line1==line2[:len_s1]:
            return len_s1
        elif len_s1>len_s2 and line1[:len_s2]==line2:
            return len_s2       
        elif  line1[count]==line2[count]:
            count=count+1
            #print(count)
            continue            
        elif line1[count]!=line2[count]:
            return count
        break


#print (singleline_diff('', 'a'))


def singleline_diff_format(line1, line2, idx):
    """
    function to highlight when a string is difference
    with the string and the reference for the difference.
    """
    if (idx>len(line1) or idx >len(line2)) or idx==-1:
        return ""
    elif "\n" in line1:
        return ""
    elif  "\n" in line2:
        return ""
    elif "\r" in line1:
        return ""
    elif "\r" in line2:
        return ""
    else:
        return(line1+"\n"+"="*idx+"^"+"\n"+line2+"\n")


def multiline_diff(lines1, lines2):
    lst_1=list()
    lst_2=list()

    for lines in lines1:
        lines=lines.strip()
        #print(lines.strip())
        lst_1.append(lines)
        return lst_1
    #return test

lines1="""Ajay was here yesterday he was at home looking after his son
           Test123"""
lines2=" "

print(multiline_diff(lines1, lines2))


