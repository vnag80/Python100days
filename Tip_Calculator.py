bill_amt = round(float(input("Enter The total bill amount")),2);
tip = int(input(" What is Tip percentage in 10 12 15?"));
member_cnt = int(input("Enter number of members "));
bill_per_person =  round((bill_amt * (1 + (tip/100))/member_cnt),2);
print(f" Pay each {bill_per_person}")
