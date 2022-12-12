student_scores={
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Nevile":62
}

student_grade={}

for student in student_scores:
    score=student_scores[student]
    if score >90:
        student_grade[student]="OutStanding"
    elif score > 80:
        student_grade[student]="Exceeds Expectation"
    elif score>70:
        student_grade[student]="Acceptable"
    else:
        student_grade[student]="Fail"

print(student_grade)
