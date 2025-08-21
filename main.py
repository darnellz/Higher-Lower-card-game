from deck_creation import Deckofcards
from betting import Betting, WinLose

def main():
    HiLo_deck = Deckofcards()

    while True:
        print(f"{len(HiLo_deck.deck)} card left")
        card1 = HiLo_deck.card_pull()
        print(f"== {card1} ==")
        bet = Betting()
        card2 = HiLo_deck.card_pull()
        print(f"== {card2} ==")
        WinLose(card1, card2, bet)
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

if __name__ == '__main__':
    main()