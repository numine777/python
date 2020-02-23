import random

money = 100

#functions
def pick_card(money):
    bet = input("Place bet: ")
    bet = int(bet)
    player_1 = draw()
    player_2 = draw()
    if player_1 > player_2:
        money += bet
    if player_2 > player_1:
        money -= bet
    else:
        money = money
    return money

def draw():
    card_points =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    random_card = random.choice(card_points)
    return random_card

#call

print("Balance: "+str(pick_card(money)))
