import random

a= input("Enter your choice?  Head/Tail   ").lower()

random_side=random.randint(0,1)
if random_side==1:
    random_side="head"
else:
    random_side="tails" 

if random_side==a:
    print("you win output came "+random_side)
else:
    print("you loss output came "+random_side)