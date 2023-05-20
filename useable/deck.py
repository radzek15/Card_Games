import random

values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
suits = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
ranks = [key for key in values.keys()]


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class FullDeck:

    def __init__(self):
        self.deck = [Card(r, s) for r in ranks for s in suits]

    def shuffle_deck(self):
        random.shuffle(self.deck)
