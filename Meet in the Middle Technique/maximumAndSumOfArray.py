class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:

        bitMaskToAndValMap = defaultdict(int)
        @lru_cache(None)
        def backtracking(andSoFar, slotNum, usedIndicesBitMask):
            if slotNum==numSlots+1:
                bitMaskToAndValMap[usedIndicesBitMask] = max(bitMaskToAndValMap[usedIndicesBitMask], andSoFar)
            else:
                backtracking(andSoFar, slotNum+1, usedIndicesBitMask)
                for index, num in enumerate(nums):
                    if not (1<<index)&usedIndicesBitMask:
                        backtracking(andSoFar + (num&slotNum), slotNum+1, usedIndicesBitMask|(1<<index))

        backtracking(0, 1, 0)
        maxAndSum, allSetBitMask = 0, (1<<len(nums))-1
        for key, val in bitMaskToAndValMap.items():
            if key^allSetBitMask in bitMaskToAndValMap:
                maxAndSum = max(maxAndSum, val+bitMaskToAndValMap[key^allSetBitMask])
        return maxAndSum