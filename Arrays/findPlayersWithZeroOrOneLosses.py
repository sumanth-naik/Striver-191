matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

def playerWithZeroOrOneLosses(matches):
    zeroLossesSet = set()
    oneLossSet = set()
    moreThanOneLossesSet = set()

    for match in matches:
        winner = match[0]
        loser = match[1]
        if winner not in moreThanOneLossesSet and winner not in oneLossSet:
            zeroLossesSet.add(winner)
        if loser in zeroLossesSet:
            zeroLossesSet.remove(loser)
            oneLossSet.add(loser)
        elif loser in oneLossSet:
            oneLossSet.remove(loser)
            moreThanOneLossesSet.add(loser)
        elif loser not in moreThanOneLossesSet:
            oneLossSet.add(loser)

    return [sorted(list(zeroLossesSet)), sorted(list(oneLossSet))]

print(playerWithZeroOrOneLosses(matches))