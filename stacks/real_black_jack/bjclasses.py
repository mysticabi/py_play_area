#!/usr/bin/env python3
import random
shapes = ('Spade' , 'Diamond' , 'Club' , 'Heart')
types = ('two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight' , 'nine'  , 'Jack' , 'Queen' , 'King' , 'Ace')
values = {"two":2 , "three":3 , "four":4 , "five":5 , "six":6 , "seven":7 , "eight":8 , "nine":9  , "Jack":10, "Queen":10 , "King":10 , "Ace":11}

class Deck():
    """
    Deck is a class that contains has methods and variables to
        1)  initialize a Deck
        2)  Shuffle a Deck
        3)  Draw card from the Deck
    """
    def __init__(self):
        self.cards = []

    def prepare_deck(self):
        self.cards.clear()
        for i in shapes:
            for j in types:
                self.cards.append(Card(i,j,values.get(j)))
        random.shuffle(self.cards)


class Card():
    """
    Card class defines a card in the deck.
    Has shape, value and type as variables.
    To initialize: (shape, type, value)
    Shape: Spade, Diamond, Club, Heart
    """

    def __init__(self, shape, type, value):
        self.shape = shape
        self.type = type
        self.value = value


class Player():
    """
    Class that defines a player and attributes associated with Player
    """

    def __init__(self, cards, credits, is_dealer, bet_amount):
        self.cards = cards
        self.credits = credits
        self.losses = 0
        self.wins = 0
        self.is_dealer = is_dealer
        self.bet_amount = bet_amount

    def addcredits(self, credits):
        self.credits += credits


    def adjustaces(self):
        if self.cardcount() >21:
            for card in self.cards:
                if card.value == 11:
                    card.value = 1

    def isbust(self):
        self.adjustaces()
        return self.cardcount()>21

    def cardcount(self):
        card_count=0
        for card in self.cards:
            card_count+= card.value
        return card_count
