import random

cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
cards_in_hand = [random.choice(cards),random.choice(cards)]
while True:
   # balance = [10]
    #print('you have 10$')
    play= input("would you like to play Black Jack?")
    #gamble = int(input('how much you bet? '))
    if play == 'yes':
        print(cards_in_hand)
    else:
        exit()

    choice = input("Add another card?")
    if choice == 'yes':
        cards_in_hand.append(random.choice(cards))
        print(cards_in_hand)
    else:
        pass

    sum_of_cards = sum(cards_in_hand)

    if sum_of_cards <= 21:
        print("You win")
       # print(f"you won {gamble}")
       # balance.append(gamble)
      #  print(sum(balance))
    else:
        print("You lose")


    answer = input(" Wanna play again? yes/no: ")
    if answer != 'yes':
        break