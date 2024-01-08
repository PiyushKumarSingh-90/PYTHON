import random
import time

print("\n\n_____________WELCOME_____________")

l=["rock","paper","scissor"]

def game(l):
    h=int(input("\nEnte your choice : (1.ROCK 2.PAPER 3.SCISSOR)"))
    if h==1:
        cho="rock"
    elif h==2:
        cho="paper"
    elif h==3:
        cho="scissor"
    else:
        print("INVALID CHOICE")    
        
    com=random.choice(l)
    time.sleep(2)
    print(f"\n\nyour choice :{cho}\ncomputer choice :{com}")
    
    if cho==com:
        print("\ntie")
        
    if ((cho=="rock"  and com=="scissor") or 
        (cho=="paper" and com=="rock") or 
        (cho=="scissor" and com=="paper")):
        print("\nYOU WIN ")
        
        
    if((cho=="rock"  and com=="paper") or 
        (cho=="paper" and com=="scissor") or 
        (cho=="scissor" and com=="rock")):
        print("\nCOMPUTER WIN")
    
    return True

# game(l)
while game(l):
    ask=input("\n\nDo u wnat to play again?(y/n)")
    if  ask=="y":
        print("\nNEXT ROUND")

    else:
        print("thank you")
        break
