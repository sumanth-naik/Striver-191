words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
from collections import Counter
import heapq

def topKFrequentWords(words, k):    
    counter = Counter(words)
    return (heapq.nsmallest(k, counter, key=lambda x:(-counter[x],x)))

print(topKFrequentWords(words, k))

nums = [1,1,1,2,2,3]
k = 2
def topKFrequentNums(nums, k: int):
    counter = Counter(nums)
    return heapq.nsmallest(k, counter, key= lambda x: -counter[x])

print(topKFrequentNums(nums, k))