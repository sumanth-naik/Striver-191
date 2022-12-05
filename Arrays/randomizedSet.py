import random
class RandomizedSet:

    def __init__(self):
        self.valuesArray = []
        self.valToIndexMap = {}

    def insert(self, val: int) -> bool:
        if not val in self.valToIndexMap:
            self.valuesArray.append(val)
            self.valToIndexMap[val] = len(self.valuesArray)-1
            return True
        return False
    
    def remove(self, val: int) -> bool:
        if val in self.valToIndexMap:
            lastValIndex = len(self.valuesArray)-1
            lastVal = self.valuesArray[lastValIndex]
            valIndex = self.valToIndexMap[val]

            self.valuesArray[lastValIndex], self.valuesArray[valIndex] = self.valuesArray[valIndex], self.valuesArray[lastValIndex]
            self.valToIndexMap[lastVal] = valIndex

            self.valuesArray.pop()
            del self.valToIndexMap[val]
            return True
        return False

    def getRandom(self) -> int:
        return self.valuesArray[random.randint(0,len(self.valuesArray)-1)]