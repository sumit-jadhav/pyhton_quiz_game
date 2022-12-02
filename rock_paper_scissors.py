import random

rock='''ROCK'''
paper='''PAPER'''
scissors='''SCISSORS'''

user_choice=int(input("Type 0 for ROCK or 1 for paper or 2 for Scissors \n "))

computer_choice=random.randint(0,2)
print(computer_choice)

if user_choice>=3 or user_choice<0:
    print("You typed a invalid number")
elif user_choice==0 and computer_choice==2:
    print("You win")
elif computer_choice == 0 and user_choice==2:
    print("you lose")
elif computer_choice>user_choice:
    print("you lose")
elif user_choice>computer_choice:
 print("You win")
elif computer_choice == user_choice:
    print("its a draw")
