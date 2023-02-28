import random
def calcdeck(deck):
    total = 0;
    for val in deck:
       if val == 11 and  (total + val) > 21:
           total += 1
       else:
           total += val
    return total

def checkforblackJack(deck):
    if len(deck) == 2 and calcdeck(deck)  == 21:
       return True
    else:
       return False



def countCards(cards):
    print("counting in progress")
deck = [11,2,3,4,5,6,7,8,9,10,10,10,10,10]
playerDeck = [];
dealerDeck = [];
a = random.randint(0,13)
playerDeck.append(deck[random.randint(0,13)]);
playerDeck.append(deck[random.randint(0,13)])
dealerDeck.append( deck[random.randint(0,13)]);
dealerDeck.append(deck[random.randint(0,13)]);
#print(playerDeck,dealerDeck)
print("Player cards:",playerDeck);
print("Dealer Open Card:", dealerDeck[0]);
if ( checkforblackJack(playerDeck) and checkforblackJack(dealerDeck)):
    print("It is draw")
    exit(0)
if (checkforblackJack(playerDeck) ):
    print(playerDeck, dealerDeck)
    print("Player Wins")
    exit(0)
if (checkforblackJack(dealerDeck)):
    print(playerDeck, dealerDeck)
    print("Dealer Wins")
    exit(0)
playerCheck = input("Enter you want to draw card Yes or No");
burst = False
while( playerCheck == "Yes" and not burst):
    playerDeck.append(deck[random.randint(0,13)])
    print("Pleayer cards and count",playerDeck,calcdeck(playerDeck))
    if calcdeck(playerDeck) > 21:
        burst = True
        print(playerDeck, dealerDeck)
        print("Player bursted with count ", calcdeck(playerDeck))
        print("Dealer Wins")
        exit(0)
    else:
        playerCheck = input("Enter you want to draw card Yes or No");


while   22 > calcdeck(dealerDeck) < 17 :
    dealerDeck.append(deck[random.randint(0, 13)])

print(playerDeck,calcdeck(playerDeck),dealerDeck,calcdeck(dealerDeck))
if calcdeck(dealerDeck) > 21:
    print("Dealer bursted with count ", calcdeck(dealerDeck))
    print("Player Wins")
elif    calcdeck(dealerDeck) > calcdeck(playerDeck):
    print("Dealer Wins")
elif  calcdeck(playerDeck) > calcdeck(dealerDeck) :
    print("Player Wins")
else:
    print("Tie")