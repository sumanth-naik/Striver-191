class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        @lru_cache(None)
        def recursion(left, right, turn):
            if left==right: return nums[left] if turn else -nums[left]
            leftPick = (nums[left] if turn else -nums[left]) + recursion(left+1, right, not turn)
            rightPick = (nums[right] if turn else -nums[right]) + recursion(left, right-1, not turn)
            return min(leftPick, rightPick) if not turn else max(leftPick, rightPick)

        return recursion(0, len(nums)-1, True)>=0


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        @lru_cache(None)
        def minimax(left, right):
            if left==right: return nums[left]
            return max(nums[left]-minimax(left+1, right), nums[right]-minimax(left, right-1))
            
        return minimax(0, len(nums)-1)>=0