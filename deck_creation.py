import random

Suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
Ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class Deckofcards():
    def __init__(self):
        self.deck = []
        self.create_deck()

    def create_deck(self):
        for suit in Suits:
            for rank in Ranks:
                self.deck.append(F"{rank} of {suit}")
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def card_pull(self):
        if len(self.deck) == 0:
            self.create_deck()
            print("--- New deck created ---")
        return self.deck.pop(0)
    
    def card_discard(self):
        for x in range(3):
            self.card_pull()
        print("=-=-=-= 3 cards discarded =-=-=-=")