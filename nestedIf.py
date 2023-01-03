height = int(input("Enter a person height in centimetor"));
if height > 120:
    age = int(input("Enter a person age"));
    if age > 18:
        print("Pay $12")
    else:
        print("Pay $7")
else:
    print("You are not eligible to ride");