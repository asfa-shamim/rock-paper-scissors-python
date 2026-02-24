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
     '''
     computer number -  your number
     '''
     if((computer-you)==-1 or(computer-you)==2 ):
       print("you win")
     else:
       print("you lose")           