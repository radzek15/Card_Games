import Deck
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_cards(self, cards):
        self.hand.extend(cards)

    def remove_card(self):
        return self.hand.pop(0)

    def __str__(self):
        return f'Player -- {self.name}'
