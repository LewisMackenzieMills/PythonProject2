from random import choice
Liquors = ["Gin", "Vodka", "Whiskey", "Rum", "Tequila", "Absinthe", "Sake", "Soju"]
from random import choice
Liquors = ["Gin", "Vodka", "Whiskey", "Rum", "Tequila", "Absinthe", "Sake", "Soju"]
from random import choice
Chasers = ["Redbull", "Cranberry Juice", "Orange Juice", "Fanta Lemon", "Fanta Orange", "Sprite"]
name = input("I am the virtual bartender. What is your name?")
legal=False
try:
    age = input("What is your age?")
    age = int(age)
    country = input("What is your country")
    legal = False
    if age >= 21:
        legal = True
    elif age >= 18 and (country != "USA" or country != "UAE" ):
        legal = True
    elif age >= 16 and country == "Luxembourg":
        legal = True
    elif age >=10000 and country == "Saudi Arabia":
        legal = True
except ValurError:
        print("Dont Play Games With Me, You Sad Little Child")
if legal:
    print("Dear", name, "Its my pleasure to serve you", choice(Liquors),"&",choice(Chasers))
else:
    print("Dear", name, "I cant serve you little baby")

import random

price = round(random.uniform(5.00, 20.00), 2)

print("Your bill is:", price, "USD")
