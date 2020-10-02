from random import randint
print("WELCOME TO ROCK, PAPER, SCISSOR\n")
player= input(" ROCK (r),Paper (p),Scissor (s)\n")

computer = randint(1,3)
if computer==1:
    computer_ch='r'
elif computer==2:
    computer_ch='p'
else:
    computer_ch='s'
    
print(computer_ch,'VS',player)

#logic

if player=='r' and computer_ch=='p':
    print("computer wins\n")
elif player=='r' and computer_ch=='s':
     print("you win \n")
elif player=='p' and computer_ch=='r':
    print("you win")
elif player=='p' and computer_ch=='s':
    print("computer win")
elif player=='s' and computer_ch=='r':
    print("computer wins")
elif player=='s' and computer_ch=='p':
    print("you win")
else:
    print("draw")
