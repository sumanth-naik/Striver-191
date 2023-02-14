from collections import Counter
def minRoundsToCompleteAllTasks(tasks):
    counter = Counter(tasks)
    totalRounds = 0
    for num in counter:
        if counter[num]==1:
            return -1
        totalRounds += (((counter[num]-1)//3)+1)
    return totalRounds