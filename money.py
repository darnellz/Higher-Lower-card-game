def Starting_cash():
    intmoney = False
    while intmoney == False:
        try:
            starting_cash = int(input("Starting amount: "))
            if starting_cash < 1:
                # i hate this many nests
                raise Exception
            intmoney = True
        except:
            print("Input a whole number greater than 1.")
    return starting_cash

def Bet_amount(money):
    betmoney = False
    while betmoney == False:
        try:
            bet_amount = int(input("                                      =+= Bet amount: "))
            if (bet_amount > money) or (bet_amount < 0):
                raise Exception
            betmoney = True
        except:
            print("Input a positive whole number less than or equal to your current money.")
    return bet_amount

def Bet_payout(money, bet_amount, WL):
    if WL == True:
        return bet_amount + money
    else:
        return money - bet_amount