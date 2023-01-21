student_scores = [35,56,36,78,25,95]
# total_students = len(student_heights)
high_score = student_scores[0];
for score in student_scores:
    if score > high_score:
        high_score = score
print(high_score);

35
56 > 35
56
36 > 56
78 > 56
78
25 > 78 
95>78
95