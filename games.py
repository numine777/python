import random

money = 100

#Write your game of chance functions here
def heads_tails(money):
    bet = input("Place bet: ")
    bet = int(bet)
    guess = input("Call Heads or Tails: ")
    guess = str(guess)
    answer = coin_toss()
    if answer == guess:
        money += bet
    elif answer != guess:
        money -= bet
    return money

def coin_toss():
    num = random.randint(1,2)
    if num == 1:
        return "Heads"
    elif num == 2:
        return "Tails"


#Call your game of chance functions here
print("Balance: "+str(heads_tails(money)))
