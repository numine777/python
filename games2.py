import random

money = 100

#Write your game of chance functions here
def cho_han(money):
    bet = input("Place bet: ")
    bet = int(bet)
    guess = input("Call Even or Odd: ")
    guess = str(guess)
    num1 = dice_roll()
    num2 = dice_roll()
    if (num1 + num2) % 2 == 0 and guess == "Even":
        money += bet
    elif (num1+ num2) % 2 == 1 and guess == "Odd":
        money += bet
    else:
        money -= bet
    return money

def dice_roll():
    num = random.randint(1,6)
    return num


#Call your game of chance functions here
print("Balance: "+str(cho_han(money)))
