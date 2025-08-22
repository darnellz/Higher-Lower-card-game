from deck_creation import Deckofcards
from betting import Betting, WinLose, Wincounter, Longwincounter
from money import Starting_cash, Bet_amount, Bet_payout

def main():
    HiLo_deck = Deckofcards()
    money = Starting_cash()
    wincount = 0
    longwin = 0
    card2 = None
    while True:
        print(f"=-=-=-=-=-= Win streak: {wincount} =-=")
        print(f"=-= Longest win streak: {longwin} =-=")
        print(f"                                      =+= Money: {money} =+=")
        bet_amount = Bet_amount(money)
        print(f"=-=-=-=-=-= {len(HiLo_deck.deck)} cards left =-=")
        card1 = HiLo_deck.card_rollover(card2)
        print(f"                                      =+= {card1} =+=")
        HiLo_deck.card_discard()
        bet = Betting()
        card2 = HiLo_deck.card_pull()
        print(f"                                      =+= {card2} =+=")
        WL = WinLose(card1, card2, bet)
        money = Bet_payout(money, bet_amount, WL)
        wincount = Wincounter(wincount, WL)
        longwin = Longwincounter(wincount, longwin)
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

if __name__ == '__main__':
    main()