#!/usr/bin/env python3
class Player():
    def __init__(self, cards, dealer=False):
        self.player_type = dealer
        self.cards = cards
