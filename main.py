import random
import os

cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
cards_in_hand = [random.choice(cards),random.choice(cards),random.choice(cards)]
#while True:
play= input("would you like to play Black Jack?")
if play == 'yes':
    print(cards_in_hand)

#if random.choice(cards) == 11:
#    print('J')


    choice = input("Add another card?")
    if choice == 'yes':
        cards_in_hand.append(random.choice(cards))
        print(cards_in_hand)
    else:
        pass

    sum_of_cards = sum(cards_in_hand)

    if sum_of_cards <= 21:
        print("You win")
    else:
        print("You lose")

# Play_again = print('Play again?')
 # if Play_again == 'Yes':
