'''
1 for rock
-1 for paper
0 for scizzer

'''
import random 



computer = random.choice([-1, 0, 1])

youstr=input("enter your choice: ")
youdict={"r":1,"p":-1,"s":0}
reversedict={1:"rock",-1:"paper",0:"scissor"}

you=youdict[youstr]

# by note you have 2 number you and computer

print(f"you choose{reversedict[you]}\n computer choose {reversedict[computer]}")

if(computer==you):
    print("its draw")
else:          
    if(computer==-1 and you==1 ): 
        print("you lose")    
    elif(computer==-1 and you==0): 
        print("you win")    
    elif(computer==1 and you==-1):
        print("you win")    
    elif(computer==1 and you==0):
        print("you lose")    
    elif(computer==0 and you==1):
        print("you win")    
    elif(computer==0 and you==-1): 
        print("you lose")    
    else:
        print ("something wrong")   