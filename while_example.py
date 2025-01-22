#you have 3 lives, you roll a dice, if you get a 6 you win
# if uou dont get a 6, you lose 1 life

from random import randint
lives = 3
while True: #as long as i have lives left
    #roll the dice
    dice = randint(1, 6)
    if dice == 6:
        print("You Rolled a 6! You win!")
        break
    lives = lives - 1
    print ("You rolled a", dice, "you have", lives, "remaining")
    if lives == 0:
        print("Game Over!")
        break
