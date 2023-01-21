student_heights = [35,56,36,78,25,95]
total_students = len(student_heights)
total_height = 0;
for student_height in student_heights:
    total_height += student_height
print(round(total_height/total_students,0));