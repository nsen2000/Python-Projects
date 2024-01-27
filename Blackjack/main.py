logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
# import clear


print(logo)

my_cards = []
dealer_cards = []
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if play == "n":
    k = input("press close to exit")

if play == "y":
    check = True
    check1 = True


def deal_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def win_check(mycards, dealercards):
    """Checks which set of cards is closer to 21"""
    mycard_total = 0
    dealercard_total = 0
    my_difference = 0
    dealer_difference = 0
    for each_card in mycards:
        mycard_total += each_card
    for each_card in dealercards:
        dealercard_total += each_card

    my_difference = abs(mycard_total - 21)
    dealer_difference = abs(dealercard_total - 21)

    return my_difference, dealer_difference


def lose_check(cards):
    """Checks the sum of each of the cards in a set of cards"""
    card_total = 0
    for each_card in cards:
        card_total += each_card
    return card_total


def print_cards(my_cards):
    for each_card in my_cards:
        print("[" + f"{each_card}" + "]")


while (check == True):
    for card in range(2):
        my_cards.append(deal_cards())
        dealer_cards.append(deal_cards())

    while (sum(dealer_cards) < 17):
        dealer_cards.append(deal_cards())

    if (sum(dealer_cards) > 21):
        print(f"Dealer's cards: {dealer_cards}")
        print(f"Dealer card total is: {lose_check(dealer_cards)}")
        print("Dealer busted. You win!")
        k = input("press close to exit")
        break

    if lose_check(my_cards) == 21:
        print(f"Your cards: {my_cards}")
        print(f"Your card total is: {lose_check(my_cards)}")
        print("You win!")
        k = input("press close to exit")
        break
    if 11 in my_cards and lose_check(my_cards) > 21:
        my_cards.remove(11)
        my_cards.append(1)

    # for each_card in my_cards:
    #   print("[" + f"{each_card}" + "]")
    print(f"Your cards: {my_cards}")
    print(f"Your card total is: {lose_check(my_cards)}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    while (check1 == True):
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            my_cards.append(deal_cards())

            print(f"Your cards: {my_cards}")
            print(f"Your card total is: {lose_check(my_cards)}")
            if lose_check(my_cards) > 21:
                print("Bust!")
                k = input("press close to exit")
                check = False
                check1 = False
        else:
            check = False
            check1 = False

if lose_check(my_cards) <= 21 and lose_check(my_cards) != 21 and lose_check(dealer_cards) <= 21:
    print(f"Your cards: {my_cards}")
    print(f"Your card total is: {lose_check(my_cards)}")

    if another_card == "n":
        my_difference, dealer_difference = win_check(my_cards, dealer_cards)
        print(f"Dealer's cards: {dealer_cards}")
        print(f"Dealer card total is: {lose_check(dealer_cards)}")

    if my_difference < dealer_difference:
        print("You win!")
        k = input("press close to exit")
    elif my_difference == dealer_difference:
        print("It's a draw!")
        k = input("press close to exit")
    else:
        print("You lose!")
        k = input("press close to exit")