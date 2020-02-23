import random

money = 100

#functions
def spin():
    wheel_values = [0,28,9,26,30,11,7,20,32,17,5,22,34,15,3,24,36,13,1,00,27,10,25,29,12,8,19,31,18,6,21,33,16,4,23,35,14,2]
    random_value = random.choice(wheel_values)
    return random_value

def roulette(money):
    bet = input("Place bet: ")
    bet = int(bet)
    guess = input("Take a guess: ")
    whirl = spin()
    if guess == "Even" and whirl != 0 and whirl % 2 == 0:
        money += bet
    elif guess == "Odd" and whirl != 0 and whirl % 2 == 1:
        money += bet
    elif int(guess) == whirl:
        money += bet * 10
    else:
        money -= bet
    return money

#call
print("Balance: "+str(roulette(money)))
