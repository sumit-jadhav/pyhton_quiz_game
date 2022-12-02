student_scores=input("Input a list of student ").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)

max_score=0

for n in student_scores:
 if n>max_score:
    max_score=n
print(max_score) 
# print(max(student_scores))