"""
1 = rock
2 = paper 
3 = seasor
"""
import random

for i in range(1 ,10):
  
    computer = random.randint(1,3)
    youstr = input("Choose the rock = r , paper = p , seasor = s :")
    dicts ={"r": 1, "p": 2,"s":3}
    dictrevs ={1: "rock", 2: "paper",3:"seasor"}
    you =dicts[youstr]
    print  (f"you choose : {dictrevs[you]}\ncomputer choose : {dictrevs[computer]}")
    
    if(computer == you):
      print("Draw the match")
    elif( computer == 1 and you == 2):
        print("you win the match")
    elif( computer == 1 and you == 3):
        print("you lose the match")
    elif( computer == 2 and you == 1):
        print("you lose the match")
    elif( computer == 2 and you == 3):
        print("you win the match")
    elif( computer == 3 and you == 1):
        print("you win the match")
    elif( computer == 3 and you == 2):
        print("you lose the match")
    else:
      print("somthing got error")
      