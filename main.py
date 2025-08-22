from deck_creation import Deckofcards
from betting import Betting, WinLose, Wincounter, Longwincounter

def main():
    HiLo_deck = Deckofcards()
    wincount = 0
    longwin = 0
    while True:
        print(f"        =-= Win streak: {wincount} =-=")
        print(f"=-= Longest win streak: {longwin} =-=")
        print(f"        =-= {len(HiLo_deck.deck)} cards left =-=")
        card1 = HiLo_deck.card_pull()
        print(f"=+=+=+=+= {card1} =+=+=+=+=")
        HiLo_deck.card_discard()
        bet = Betting()
        card2 = HiLo_deck.card_pull()
        print(f"== {card2} ==")
        WL = WinLose(card1, card2, bet)
        wincount = Wincounter(wincount, WL)
        longwin = Longwincounter(wincount, longwin)
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

if __name__ == '__main__':
    main()