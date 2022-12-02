fruits=["Apple","mango","pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")


# for number in range(1,11,3):
#     print(number)

total=0
for num in range(1,101):
 total+=num
print(total)

# total_even=0
# for num in range(2,101,2):
#     total_even += num
# print(total_even)
total_even=0
for num in range(1,101):
 if num%2==0:
    total_even+=num
print(total_even)