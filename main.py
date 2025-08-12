import random

Suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
Ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class Deckofcards:
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle_deck()
    
    def create_deck(self):
        for suit in Suits:
            for rank in Ranks:
                self.cards.append(f"{rank} of {suit}")

    def shuffle_deck(self):
        random.shuffle(self.cards)

deck_1 = Deckofcards()
print(deck_1.cards)