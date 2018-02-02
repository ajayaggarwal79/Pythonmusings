def multiline_diff(lines1, lines2):
    lst=list()
    lst1=list()
    

    for word in lines1:
        word.split()
        lst=lst.append(word)
    



###lines1="""Ajay was here yesterday he was at home looking after his son
##           Test123"""
##lines2=" "
##
##
lines1="""engineering classes
science classes
"""
#lines2="//gblonhome03/aggara1/Desktop/Python/file13.txt"
print(multiline_diff(lines1, ['b']))
