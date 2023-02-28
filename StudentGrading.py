student_Scores = {"harry": 71,
"Venkat": 85,
"Sravanthi": 15,
"Sanvi": 95};
student_grades = {}
for student in student_Scores:
    if student_Scores[student] > 90:
        student_grades[student] = "Outstanding"
    elif  student_Scores[student] > 80:
        student_grades[student] = "First Class"
    elif   student_Scores[student] > 70:
        student_grades[student] = "Just Pass"
    elif   student_Scores[student] < 40:
        student_grades[student] = "Fail"

print(student_grades)
