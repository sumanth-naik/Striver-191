class Solution:
    def totalFruit(self, fruits):
        fruitToLastSeenIndexMap = {}
        firstIndexInSubarray, maxFruitsInBasket = 0, 0
        for index, fruit in enumerate(fruits):
            if fruit in fruitToLastSeenIndexMap or len(fruitToLastSeenIndexMap)<2:
                fruitToLastSeenIndexMap[fruit] = index
            else:
                minIndexOfFruitThatAreInBasket = min(fruitToLastSeenIndexMap.values())
                del fruitToLastSeenIndexMap[fruits[minIndexOfFruitThatAreInBasket]]
                fruitToLastSeenIndexMap[fruit] = index
                firstIndexInSubarray = minIndexOfFruitThatAreInBasket + 1
            maxFruitsInBasket = max(maxFruitsInBasket, index - firstIndexInSubarray + 1)
        return maxFruitsInBasket