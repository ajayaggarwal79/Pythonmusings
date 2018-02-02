score=input("Enter Score")
try:
    inp=float(score)
    if(inp < 0.6):
        print("F")
     elif(inp>=0.6 and inp<0.7):
         print("D")
     elif (inp>=0.7 and inp<0.8):
         print("C")
     elif (inp>=0.8 and inp<0.9):
         print("B")
     elif (inp>=0.9 and inp<1.0):
         print("A")    

         

except:
    print("Bad score")
