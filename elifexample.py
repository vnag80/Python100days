height = int(input("Enter a person height in centimetor"));
if height > 120:
    age = int(input("Enter a person age"));
    bill = 0
    if age < 12:
        bill = 5
        print("Pay $5")
    elif age <= 18:
        bill = 7;
        print("Pay $7")
    else:
        bill = 12;
        print("Pay $12")
    want_photo = input(" Do you want to take a photo Press Y for yes and N for NO")
    if want_photo == 'Y':
        bill = bill+ 3
    print(f"Your bill amount is {bill}$")

else:
    print("You are not eligible to ride");