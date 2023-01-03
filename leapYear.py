year = int(input("Enter the year to check is it Leap year or not"))
if year % 400 == 0:
    print("This is Leap year")
elif year % 100 == 0:
    print("This is not Leap Year")
elif year % 4 == 0:
    print("This is leap year")
else:
    print("This is not leap Year")