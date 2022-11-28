print("welcome to my computer quiz!!")

playing = input("DO you want to play?  yes/no...  ")

if playing.lower() !="yes": 
    quit()
score = 0

print("okay !! lets play :) ")

answer =input ("what does CPU stands for?  ")
if answer.lower()=="central processing unit":
    print("correct")
    score += 1
else: print("incorrect")

answer =input ("what does GPU stands for?  ")
if answer.lower()=="graphics processing unit":
    print("correct")
    score += 1
else: print("incorrect")

answer =input ("what does RAM stands for?  ")
if answer.lower()=="random access memory":
    print("correct")
    score += 1

else: print("incorrect")

answer =input ("what does ROM stands for?  ")
if answer.lower()=="read only memory":
    print("correct")
    score += 1
else: print("incorrect")


answer =input ("what does PSU stands for?  ")
if answer.lower()=="power supply unit":
    print("correct")
    score += 1
else: print("incorrect")

print("You got "+str(score)+"question correct")
