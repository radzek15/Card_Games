from Card import Card
import random
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
suits = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
ranks = [key for key in values.keys()]
class Deck:

#specyfying creating all 52 card
    def __init__(self):
        self.deck = [Card(r, s) for r in ranks for s in suits]

#function to randomly shuffle deck
    def shuffle(self):
        random.shuffle(self.deck)