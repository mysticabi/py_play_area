#!/usr/bin/env python3

from bjclasses import *
import sys
import random
import subprocess as sp

deck = Deck()
deck.prepare_deck()
gambler = Player([],0,False,1)
dealer = Player([],0,True,1)

def endgame():
    print('Your Credits: {}'.format(gambler.credits))
    print('Ending Game, Bye!')
    sys.exit(0)

def takegamblerinput():
    player_input = ''

    if gambler.credits == 0:
        player_input = input("Add Credits (enter a number to add credits), hit any other key to exit : ")
    else:
        player_input = input("Add Credits (enter a number), Continue (hit c), Exit (hit x) : ")

    try:
        if player_input in ['c', 'C']:
            pass
        elif player_input in ['x', 'X']:
            endgame()
        else:
            gambler.credits+= int(player_input)
            print("Gambler's total credit: {}".format(gambler.credits))
    except:
        endgame()
    finally:
        if gambler.credits < 1:
            print('You do not have enough credits to play, Bye!')
            endgame()

def dealcards():
    gambler.cards = []
    dealer.cards = []
    gambler.cards.append(deck.cards.pop())
    dealer.cards.append(deck.cards.pop())
    gambler.cards.append(deck.cards.pop())
    dealer.cards.append(deck.cards.pop())

def display_cards(cards, hide_last_card):
    print("______________________")
    if not hide_last_card:
        print("    Player Cards  ")
        print_str = ''
        for card in cards:
            print_str += '-- { [ ' + card.type + ' ], [ ' + card.shape + ' ], [' + str(card.value) + ' ], } -- |||'
        print_str += ' }---'
        print(print_str)
    else:
        print("    Dealer Cards  ")
        print_str = '-- { [ ' + cards[0].type + ' ], [ ' + cards[0].shape + ' ], [' + str(cards[0].value) + ' ], } -- ||| --- { Last Card Hidden } ---'
        print(print_str)
    print("______________________")

def hit_or_stand():
    while True:
        game_input = input('h for Hit or s for Stand : ')
        if game_input in ['h', 'H']:
            gambler.cards.append(deck.cards.pop())
            display_cards(gambler.cards, False)
            gambler.adjustaces()
            display_cards(gambler.cards, False)
        elif game_input in ['s', 'S']:
            display_cards(gambler.cards, False)
            break
        else:
            print('Please enter correct input')

def playdealer():
    while True:
        if dealer.isbust():
            return True
        elif dealer.cardcount() > gambler.cardcount() and dealer.cardcount() <= 21:
            return False
        else:
            dealer.cards.append(deck.cards.pop())



def main():


    while True:
        #Re-Initialize deck
        if len(deck.cards) < 10:
            deck.prepare_deck


        takegamblerinput()

        #Add code here to add logic for taking input for number of bets

        dealcards()

        display_cards(gambler.cards, False)

        display_cards(dealer.cards, True)

        gambler.adjustaces()

        hit_or_stand()

        if gambler.isbust():
            print('Gambler Bust! Card Count: {}'.format(gambler.cardcount()))
            gambler.credits -= 1
            continue

        if playdealer():
            print('Dealer Bust! Card Count: {}'.format(dealer.cardcount()))
            print('Gambler Won! Card Count: {}'.format(gambler.cardcount()))
            gambler.credits += 1
            continue
        else:
            print('Dealer Won! Card Count: {}'.format(dealer.cardcount()))
            print('Gambler Lost! Card Count: {}'.format(gambler.cardcount()))
            gambler.credits -= 1
            continue


if __name__ == '__main__':
    main()
