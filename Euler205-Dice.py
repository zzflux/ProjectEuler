#Project Euler problem #205
#Dice game
#Status: solved
#Notes: check rounding

import datetime

def diceSet(numFaces, numDice):
    dice = [1] * numDice
    first = True
    yield sum(dice)
    while first or not all([n == 1 for n in dice]):
        first = False
        for i in range(len(dice) - 1, -1, -1):
            dice[i] += 1
            if dice[i] > numFaces:
                dice[i] = 1
                continue
            else:
                yield sum(dice)
                break
    return

PSIDES = 4
PDICE = 9
CSIDES = 6
CDICE = 6

if __name__ == "__main__":
    print("Started!")
    print(datetime.datetime.now().time().isoformat())
    print("Caching...", end='')
    peteMax = max(diceSet(PSIDES, PDICE))
    colinMax = max(diceSet(CSIDES, CDICE))
    peteWinScenarios = [sum([pScore > cScore for cScore in diceSet(CSIDES, CDICE)]) for pScore in range(peteMax + 1)]
    peteLossScenarios = [sum([pScore < cScore for cScore in diceSet(CSIDES, CDICE)]) for pScore in range(peteMax + 1)]
    tieScenarios = [sum([pScore == cScore for cScore in diceSet(CSIDES, CDICE)]) for pScore in range(peteMax + 1)]
    print("done")
    print("Calculating...", end='')
    wins = sum([peteWinScenarios[n] for n in diceSet(PSIDES, PDICE)])
    losses = sum([peteLossScenarios[n] for n in diceSet(PSIDES, PDICE)])
    ties = sum([tieScenarios[n] for n in diceSet(PSIDES, PDICE)])
    total = (PSIDES ** PDICE) * (CSIDES ** CDICE)
    print("done")
    print("wins:", wins)
    print("losses:", losses)
    print("ties:", ties)
    print("wins + losses + ties:", wins + losses + ties)
    print("alleged total:", total)
    print("wins/total:", wins/total)
    print("wins/(wins + losses):", wins/(wins + losses))

#done
