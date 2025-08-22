from deck_creation import Deckofcards
from betting import Betting, WinLose

def main():
    HiLo_deck = Deckofcards()
    wincount = 0

    while True:
        print(f"=-= Win streak: {wincount} =-=")
        print(f"=-= {len(HiLo_deck.deck)} cards left =-=")
        card1 = HiLo_deck.card_pull()
        print(f"==== {card1} ====")
        HiLo_deck.card_discard()
        bet = Betting()
        card2 = HiLo_deck.card_pull()
        print(f"== {card2} ==")
        wincount = WinLose(card1, card2, bet, wincount)
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

if __name__ == '__main__':
    main()