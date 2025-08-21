from deck_creation import Ranks

def Betting():
    print("Higher, Lower, Snap bet")
    bet = input(":")
    bet = bet.lower()
    if bet == "higher":
        print("==== higher ====")
    elif bet == "lower":
        print("==== lower ====")
    elif bet == "snap":
        print("==== snap bet ====")
    else:
        raise Exception("====input higher, lower, or snap====")
    return bet

def get_rank(card):
    card_pop = []
    card_pop = card.split()
    return card_pop.pop(0)

def bet_answer(card1, card2):
    if card1 == card2:
        return "snap"
    elif card1 < card2:
        return "higher"
    elif card1 > card2:
        return "lower"
    else:
        raise Exception("File 'betting', def 'bet_answer'")

def WinLose(card1, card2, bet):
    card1_rank = get_rank(card1)
    card2_rank = get_rank(card2)
    card1_index = Ranks.index(card1_rank)
    card2_index = Ranks.index(card2_rank)
    answer = bet_answer(card1_index, card2_index)
    if bet == answer:
        print("============ WIN ============")
    else:
        print("============ LOSE ============")