import random
name_string =input ("Give me everybody names,seperated by a comma. ")

names =name_string.split(",")

random_choice=random.randint(0,len(names)-1)

print("person who is gonna pay is"+ names[random_choice]+"!")

person_who_will_pay=random.choice(names)

print("person who is gonna pay is"+ person_who_will_pay+"!")
