class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return not len(nums)&1 or reduce(xor, nums)==0 
        