## the objective of the function is to determine the bankroll from a a series 
## of best. The function takes an inital bankroll and string representing  
## the result of the game (i.e. W/L) 
## If the outcome is a 'W', then the bet is reset to 1. 
## If the outcome is a 'L', then the bet size is doubled.
## If the bet size is greater than the bankroll then the game ends. 

def f(initialAmount, betResults):

    def aux(bet, bankroll, results):
        if(bet > bankroll or len(results) == 0 ):
            return bankroll
        else:
            if results[0] == "L":
                bankroll = bankroll - bet
                newBet = 2*bet
                return aux(newBet,bankroll,results[1:])
            else:
                return aux(1,bankroll + bet, results[1:])

    return aux(1,initialAmount, betResults)

def test():
    print f(12,"WWWWWWWW")

    print f(15,"LLLWLLLL")
