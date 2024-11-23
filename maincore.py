print("\n" * 40)
print("\033c\033[3J", end='')


print('''
  ____  _               _____ _  __    _         _____ _  __
 |  _ \| |        /\   / ____| |/ /   | |  /\   / ____| |/ /
 | |_) | |       /  \ | |    | ' /    | | /  \ | |    | ' / 
 |  _ <| |      / /\ \| |    |  < _   | |/ /\ \| |    |  <  
 | |_) | |____ / ____ \ |____| . \ |__| / ____ \ |____| . \ 
 |____/|______/_/    \_\_____|_|\_\____/_/    \_\_____|_|\_\
                                                            
                                                            

''')
print("2024* made by Jonathan Luong")
m = input("Press y to start (n to close): ").lower()
if m == "y" and m.isalpha():
    pass
else:
    quit()


import random
import time

game_over = True
still_on = True


card_art = [
    ["""
    .------.
    |2--.  |
    | (\/) |
    | :\/: |
    | '--'2|
    `------'
    """],
    ["""
    .------.
    |3--.  |
    | :(): |
    | ()() |
    | '--'3|
    `------'
    """],
    ["""
    .------.
    |4--.  |
    | :/\: |
    | :\/: |
    | '--'4|
    `------'
    """],
    ["""
    .------.
    |5--.  |
    | :/\: |
    | (__) |
    | '--'5|
    `------'
    """],
    ["""
    .------.
    |6--.  |
    | (\/) |
    | :\/: |
    | '--'6|
    `------'
    """],
    ["""
    .------.
    |7--.  |
    | :(): |
    | ()() |
    | '--'7|
    `------'
    """],
    ["""
    .------.
    |8--.  |
    | :/\: |
    | :\/: |
    | '--'8|
    `------'
    """],
    ["""
    .------.
    |9--.  |
    | :/\: |
    | (__) |
    | '--'9|
    `------'
    """],
    ["""
    .------.
    |10--  |
    | :/\: |
    | (__) |
    | '-'10|
    `------'
    """],
    ["""
    .------.
    |11-.  |
    | :/\: |
    | (__) |
    | '-'11|
    `------'
    """],
    ["""
    .------.
    |J--.  |
    | :(): |
    | ()() |
    | '--'J|
    `------'
    """],
    ["""
    .------.
    |Q--.  |
    | (\/) |
    | :\/: |
    | '--'Q|
    `------'
    """],
    ["""
    .------.
    |K--.  |
    | :/\: |
    | :\/: |
    | '--'K|
    `------'
    """]
]
print("\n" * 40)
def display_cards(cards):
    lines = []
    for card in cards:
        art_lines = card_art[card-2][0].split('\n')
        if not lines:
            lines = [''] * len(art_lines)
        for i, line in enumerate(art_lines):
            lines[i] += line
    print('\n'.join(lines))

def change(a, b):
    ace_art = [
    ["""
    .------.
    |1--.  |
    | :/\: |
    | (__) |
    | '--'1|
    `------'
    """],
    ]
    if a > 21 and 11 in user_card:
        user_card.remove(11)
        user_card.append(1)
        card_art[-1] = ace_art[0]
        print("User has an Ace and it was converted from 11 to 1")
    elif b > 21 and 11 in computer_card:
        computer_card.remove(11)
        computer_card.append(1)
        card_art[-1] = ace_art[0]
        print("Computer has an Ace and it was converted from 11 to 1")


def new_r(a):
    ask = input("New rounds?(y/n): ").lower()
    if ask.isalpha() and ask == "y":
        a = True
        print("\033c\033[3J", end='')
    elif ask.isalpha() and ask == "n":
        print("\033c\033[3J", end='')
        if user_money > orin:
            print("Congrats you have made ", (user_money - orin), "$")
        elif user_money < orin:
            print("You have lost ", (orin - user_money), "$")
        else:
            print("same amount of money duh")
        a = False
        print("2024* made by Jonathan Luong")
        quit()
    else:
        quit()

#original money to compare later
orin = 500000

#Bank
user_money = 500000
computer_money = 500000

while game_over:
    print("\033c\033[3J", end='')
    #check the amount of money first
    print("\nYour balance: >>> ", user_money, "$\n")
    print("\nTarget balance: >>> ", computer_money, "$\n")

    if user_money == 0:
        print("You have ran out of money")
        quit()
    if computer_money == 0:
        print("computer lose all its money")
        quit()
    else:
        pass

    #random function
    def ran():
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        card = random.choice(cards)
        return card

    #Deposit cards
    user_card = []
    computer_card = []
    why = []

    #First 2 cards for both computer and player
    for i in range(2):
        m = ran()
        n = ran()
        computer_card.append(m)
        user_card.append(n)
        why.append('?')

    to_c = sum(computer_card)
    to_u = sum(user_card)

    print("Your card is: >>> ", user_card)
    display_cards(user_card)
    print("Computer card is >>> ", why)

    m_an = True
    while m_an:
        m = input("Do you want to get more cards? (y/n): ").lower()
        if m.isalpha() and m == "y":
            m = ran()
            user_card.append(m)
            print("Your card is: >>>")
            display_cards(user_card)
            to_u += m
            change(to_u, to_c)
            if sum(user_card) > 21:
                m_an = False
        elif m.isalpha() and m == "n":
            m_an = False
        else:
            quit()

        print("Target is thinking....")
        time.sleep(2)
        if to_c > 21:
            m = ran()
            computer_card.append(m)
            to_c += m
            change(to_u, to_c)
            why.append('?')
            print("Target decided to pick one more card\n")
        else:
            print("Target choose to stay\n")
            pass

    n = input("Check? (y/n): ").lower()
    if n == "y":
        to_un = sum(user_card)
        to_cn = sum(computer_card)

        print("Your cards >>> ", user_card)
        display_cards(user_card)
        print("\nTarget cards >>> ",computer_card, end = "")
        display_cards(computer_card)

        if to_un > to_cn and to_un <= 21:
            user_money += 500 * len(computer_card)
            computer_money -= 500 * len(computer_card)
            print("You win")
        elif to_un < to_cn and to_cn <= 21:
            user_money -= 500 * len(user_card)
            computer_money += 500 * len(user_card)
            print("Target win")
        if to_un > to_cn and to_un > 21:
            user_money -= 500 * len(user_card)
            computer_money += 500 * len(user_card)
            print("Target win")
        elif to_un < to_cn and to_cn > 21:
            user_money += 500 * len(computer_card)
            computer_money -= 500 * len(computer_card)
            print("You win")
        elif to_un == to_cn:
            print("Draw")

        print("\nYour balance: >>> ", user_money, "$\n")
        print("\nTarget balance: >>> ", computer_money, "$\n")
        new_r(game_over)
    else:
        new_r(game_over)
