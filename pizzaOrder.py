print("Welcome to the Python Pizza \n")
size = input("What size pizza would you like to order small ,medium or Large S,M OR L");
price = 0;
extra_peproni = input("Would you like to add extra Peproni Y or N");
extra_cheese = input("Would you like to have extra chees Y or N");
if size == "S":
    price = 15
    if extra_peproni == "Y":
        price += 2;
else:
    if size == "M":
      price = 20
    if size == "L":
      price = 25
    elif extra_peproni == "Y":
        price += 3;
    else:
        print("Invalid Size")
if extra_peproni == "Y":
        price += 1;
print(f"Your todal order costs you ${price}");