name1 = input("Enter first name ").lower()
name2 = input("Enter Second name").lower()
combine_name = name1 + name2
true_Score = combine_name.count("t") + combine_name.count('r') + combine_name.count('u') + combine_name.count('e');
Love_score = combine_name.count("l") + combine_name.count('o') + combine_name.count('v') + combine_name.count('e');
final_score = true_Score * 10 + Love_score;
print(final_score);
if final_score < 10 and final_score > 90:
    print(f"your score is {final_score}, you go together coke and mentos")
elif final_score < 40 and final_score > 50:
    print(f"your score is {final_score}, you are alright together")
else:
    print(f"your score is {final_score}")
