from deck_creation import Ranks

def Betting():
    correct_input = False
    print("higher, lower, snap bet")
    while correct_input == False:
        bet = input(": ")
        bet = bet.lower()
        if (bet != "higher") and (bet != "lower") and (bet != "snap") and (bet != "h") and (bet != "l") and (bet != "s"):
            print("==== input higher, lower, or snap ====")
        else:
            correct_input = True
    if (bet == "higher") or (bet == "h"):
        return "higher"
    elif (bet == "lower") or (bet == "l"):
        return "lower"
    elif (bet == "snap") or (bet == "s"):
        return "snap"

def get_rank(card):
    card = card.split()
    return card.pop(0)

def bet_answer(card1, card2):
    if card1 == card2:
        return "snap"
    elif card1 < card2:
        return "higher"
    elif card1 > card2:
        return "lower"

def WinLose(card1, card2, bet):
    card1_rank = get_rank(card1)
    card2_rank = get_rank(card2)
    card1_index = Ranks.index(card1_rank)
    card2_index = Ranks.index(card2_rank)
    answer = bet_answer(card1_index, card2_index)
    if bet == answer:
        print("============================ WIN ============================")
        return True
    else:
        print("============================ LOSE ===========================")
        return False
    
def Wincounter(wincount, WL):
    if WL == True:
        wincount += 1
        return wincount
    else:
        wincount = 0
        return wincount
    
def Longwincounter(wincount, longwin):
    if wincount > longwin:
        longwin = wincount
    return longwin