import random
# from random import choice
# from random import randint

# coin = random.choice(["Heads", "Tails"])
# coin = choice(["Heads", "Tails"])
# print(coin)

# number = random.randint(1, 100)
# number = randint(1, 100)
# print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
print(cards)
for card in cards:
    print(card)