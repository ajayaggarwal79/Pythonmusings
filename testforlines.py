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
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """

    line1 = lines1
    line2 = lines2
    mincount=min(len(line1), len(line2))
    #print(mincount)

    if singleline_diff(line1, line2) <mincount:
        if len(lines1) != len(lines2):
            ln_num = singleline_diff(line1, line2)
            print(ln_num)

            line1 = lines1[singleline_diff(line1, line2)]
            line2 = lines2[singleline_diff(line1, line2)]
            idx_num = singleline_diff(line1, line2)
            return (ln_num, idx_num)


        elif len(lines1) == len(lines2): 
            ln_num = singleline_diff(line1, line2)

            line1 = lines1[singleline_diff(line1, line2)]

            line2 = lines2[ln_num]

            idx_num = singleline_diff(line1, line2)
            return (ln_num, idx_num)
    elif lines1==lines2 or (len(lines1)==0 and len(lines2)==0):
        return -1,-1
    elif len(line1)<len(line2) and line1==line2[:len(line1)]:
        idx_num = singleline_diff(line1, line2[:len(line1)])
        return len(line1), idx_num+1
    elif len(line1)>len(line2) and line1[:len(line2)]==line2:
        idx_num = singleline_diff(line2[:len(line1)], line2)
        return len(line2), idx_num+1



##lines1=[""""Ajay Was her
##        test123"""]
##lines2=['b']
##
print(multiline_diff( [''], ['']))




def get_file_lines(filename):
    """
    Get the input from a file and store the lines off
    """
    #filename.rsplit()
    List = open(filename).read().splitlines()
    return List
    
#print(get_file_lines("C:/Users/ajaya/Desktop/py4e/file1.txt"))

