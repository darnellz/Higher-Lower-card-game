import random

Suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
Ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class Deckofcards:
    def __init__(self):
        self.cards = []
        self.create_deck()
    
    def create_deck(self):
        for suit in Suits:
            for rank in Ranks:
                self.cards.append(f"{rank} of {suit}")

    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    def fist_card_pull(self):
        if len(self.cards) < 2:
            raise NameError("too few cards")
        return self.cards.pop()
    
    def second_card_pull(self):
        return self.cards.pop()
    
    def outcome(self, first_card, second_card, bet):
        first_rank = get_rank(first_card)
        second_rank = get_rank(second_card)
        first_index = Ranks.index(first_rank)
        second_index = Ranks.index(second_rank)
        higher = self.higher(first_index, second_index)
        lower = self.lower(first_index, second_index)
        snap = self.snap_bet(first_index, second_index)
        answer = HLS_answer(higher, lower, snap)
        win_lose(bet, answer)

    def snap_bet(self, first, second):
        return (
            first == second
        )
    
    def higher(self, first, second):
        return (
            first < second
        )
    
    def lower(self, first, second):
        return (
            first > second
        )

def win_lose(bet, answer):
    if bet == answer:
        print("====Win====")
    else:
        print("====Lose====")

def HLS_answer(high, low, snap):
    if high == True:
        print("====Higher====")
        return "h"
    elif low == True:
        print("====Lower====")
        return "l"
    elif snap == True:
        print("====Snap====")
        return "s"
    else:
        raise NameError("HLS_answer unknown")

def get_rank(card):
    list = []
    list = card.split()
    return list.pop(0)

def HLS_bet(input):
    low_inp = input.lower()
    if low_inp == "h":
        print("====Higher====")
    elif low_inp == "l":
        print("====Lower====")
    elif low_inp == "s":
        print("====Snap bet====")
    else:
        raise NameError("input H, L, or S")
    return low_inp

def main():
    deck_1 = Deckofcards()
    deck_1.shuffle_deck()
    first_card = deck_1.fist_card_pull()
    print(first_card)
    print("(H)igher, (L)ower, (S)nap bet")
    bet = HLS_bet(input(":"))
    second_card = deck_1.second_card_pull()
    print(second_card)
    outcome = deck_1.outcome(first_card, second_card, bet)

main()