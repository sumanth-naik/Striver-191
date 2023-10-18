import random
class RandomizedCollection:

    def __init__(self):
        self.valuesArray = []
        self.valuesToIndicesSetMap = {}

    def insert(self, val: int) -> bool:
        if not val in self.valuesToIndicesSetMap:
            self.valuesToIndicesSetMap[val] = set([len(self.valuesArray)])
            self.valuesArray.append(val)
            return True
        else:
            self.valuesToIndicesSetMap[val].add(len(self.valuesArray))
            self.valuesArray.append(val)
            return False

    def remove(self, val: int) -> bool:
        if val in self.valuesToIndicesSetMap:
            lastValIndex = len(self.valuesArray) - 1
            lastVal = self.valuesArray[lastValIndex]
            # next(iter()) is not a great idea
            valIndex = self.valuesToIndicesSetMap[val].pop()

            self.valuesArray[lastValIndex], self.valuesArray[valIndex] = self.valuesArray[valIndex], self.valuesArray[lastValIndex]
            if not lastValIndex==valIndex:
                self.valuesToIndicesSetMap[lastVal].remove(lastValIndex)
                self.valuesToIndicesSetMap[lastVal].add(valIndex)

            self.valuesArray.pop()

            if len(self.valuesToIndicesSetMap[val])==0:
                del self.valuesToIndicesSetMap[val]

            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.valuesArray[random.randint(0,len(self.valuesArray)-1)]
        
