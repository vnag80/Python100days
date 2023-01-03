print(" Welcome to Tresure Island. Your mission is find the treasure");
direction = input(" Enter left or right");
if direction == "left":
  action = input("Enter you like to swim or wait")
  if action == "wait":
     door = input("Enter which door would you like to choose Blue Red Yellow")
     if door == 'yellow':
         print("You win")
     else:
         print("Game over")
  else:
      print("Game Over")

else:
    print("Game Over")