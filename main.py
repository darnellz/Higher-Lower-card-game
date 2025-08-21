from deck_creation import Deckofcards
from betting import Betting, WinLose

def main():
    HiLo_deck = Deckofcards()
    HiLo_deck.create_deck()

    while True:
        card1 = HiLo_deck.card_pull()
        print(card1)
        bet = Betting()
        card2 = HiLo_deck.card_pull()
        print(card2)
        WinLose(card1, card2, bet)

main()