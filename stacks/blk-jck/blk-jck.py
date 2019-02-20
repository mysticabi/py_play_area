#!/usr/bin/env python3
from player import Player
import subprocess as sp
import random

cards=[2,3,4,5,6,7,8,9,10,10,10,11]


def print_card(card):
    print("  ------------------ ")
    print(" ")
    print("           {}    ".format(card))
    print(" ")
    print("  ------------------ ")

def display_cards(player):
    print("--------------------------")
    if(player.player_type):
        print("     Dealer Cards     ")
        print_card(player.cards[0])
        print_card('X')
        print("--------------------------")
    else:
        print("      Gambler Cards     ")
        for i in player.cards:
            print_card(i)
        print("--------------------------")

def play_dealer():#Play dealer's game
    while sum(dealer.cards)<=21:
        if sum(dealer.cards) > sum(gambler.cards) and  sum(dealer.cards) <=21:
            return False
        elif sum(dealer.cards) > 21:
            return True
        else:
            dealer.cards.append(random.choice(cards))
            if sum(dealer.cards) >21:
                return True


def bust_or_not(cards):#evaluate the cards
    if sum(cards) > 21 and cards[len(cards)-1] == 11:
        cards[len(cards)-1] = 1
        if sum(cards) > 21: return True
        else: return False
    else: return False

def clear_board():
    sp.call('clear',shell=True)
    display_cards(dealer)
    display_cards(gambler)


gambler=Player([], False)
dealer=Player([], True)
gambler_wins = 0
gambler_losses = 0

def main():
    global gambler_wins
    global gambler_losses
    is_gambler_bust = False
    is_dealer_bust  = False
    #Assign two cards to gambler
    gambler.cards.append(random.choice(cards))
    gambler.cards.append(random.choice(cards))
    if gambler.cards.count(11) >= 2:
        gambler.cards[0] = 1
    #Assign two cards to dealer
    dealer.cards.append(random.choice(cards))
    dealer.cards.append(random.choice(cards))
    display_cards(gambler)
    display_cards(dealer)

    while True:
        print("------------------------------------------------")
        print("--------------  Begin Game  --------------------")
        h_or_s=input("Mr Gambler: Hit or Stand (h for hit, s for stand)")
        if h_or_s not in ['h','s']:
            print("   Choose Wisely Gambler -- h or s --")
            continue
        elif h_or_s is 'h':
            gambler.cards.append(random.choice(cards))
            clear_board()
            if sum(gambler.cards) > 21:
                if gambler.cards[:] == 11:
                    gambler.cards[:] = 1
                else:
                    is_gambler_bust = True
                    break
        else:
            print("   ----- Now Dealer Plays -----   ")
            is_dealer_bust =  play_dealer()
            print("Dealer Cards: {}, dealer total {}".format(dealer.cards,sum(dealer.cards) ))
            break

    if is_gambler_bust:
        print("   ----- Gambler bust -------   ")
        print("     Better Luck Next Time    ")
        gambler_losses += 1
    elif is_dealer_bust:
        print("   ----- Dealer Bust -------")
        print("   Congratulations, you won!")
        gambler_wins+= 1
    elif sum(dealer.cards) > sum(gambler.cards):
        print("   ----- Gambler bust -------   ")
        print("     Better Luck Next Time    ")
        gambler_losses += 1
    else:
        print("   ----- Dealer Bust -------")
        print("   Congratulations, you won!")
        gambler_wins+= 1

    i_p = input("Mr Gambler: Do you want to gamble gain? Press any key, q to quit")
    if i_p is not 'q':
        del dealer.cards[:]
        del gambler.cards[:]
        is_gambler_bust = False
        is_dealer_bust = False
        main()
    else:
        print('You lost {} times and you won {} times'.format(gambler_losses, gambler_wins))

if __name__ == '__main__':
    main()
