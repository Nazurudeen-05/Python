# THis program is used to count the number of vowels,consonants,integers and special characters in a given sentence
def vowelcount(str):
    v=0
    c=0
    s=0
    int=0
    for i in range (0,len(str)):
        ch=str[i]
        if(ch>="a" and ch<="z" or ch>="A" and ch<="Z"):
           ch=ch.lower()
           if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch =="u"):
               v=v+1   
           else:
               c=c+1
        elif(ch>="1" and ch<="9"):
            int=int+1
        else:
            s=s+1    
    print("vowels:",v,
          "integers:",int,
          "special characters:",s,
          "consonants:",c,
          )

str="123geeksforgeeks@@@"
vowelcount(str)
