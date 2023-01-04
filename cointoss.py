import random
user_input = input(" Enter Heads or Tails");
actual = random.randint(0,1);
print(actual)
if (actual == 0 and user_input == "Heads") or (actual == 1 and user_input == "Tails"):
    print('you win')
else:
    print('You lost')
