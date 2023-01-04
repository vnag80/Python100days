import random
first_player = input("Enter the first player name: \n");
second_player = input("Enter the second player name: \n");
first_player_choice = random.randint(0,2);
second_player_choice = random.randint(0,2);
options = ['rock','paper','scissors'];
print(first_player + ' Choosen ' + options[first_player_choice])
print(second_player + ' Choosen ' + options[second_player_choice])
if options[first_player_choice] == 'rock':
    if options[second_player_choice] == 'rock':
        print('No body win');
    if options[second_player_choice] == 'paper':
        print(second_player + ' Win');
    if options[second_player_choice] == 'scissors':
        print(first_player + ' Win');
if options[first_player_choice] == 'paper':
    if options[second_player_choice] == 'paper':
        print('No body win');
    if options[second_player_choice] == 'scissors':
        print(second_player + ' Win');
    if options[second_player_choice] == 'rock':
        print(first_player + ' Win');
if options[first_player_choice] == 'scissors':
    if options[second_player_choice] == 'scissors':
        print('No body win');
    if options[second_player_choice] == 'rock':
        print(second_player + ' Win');
    if options[second_player_choice] == 'paper':
        print(first_player + ' Win');