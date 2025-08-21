def Betting():
    print("Higher, Lower, Snap bet")
    bet = input(":")
    bet = bet.lower()
    if bet == "higher":
        print("====HIGHER====")
    elif bet == "lower":
        print("====LOWER====")
    elif bet == "snap":
        print("====SNAP BET====")
    else:
        print("====input higher, lower, or snap====")
    return bet

def WinLose(card1, card2, bet):