from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y): return int(y+x)-int(x+y)
        return ''.join(sorted(map(str, nums), key=cmp_to_key(compare))) if any(num>0 for num in nums) else "0"

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return ''.join(sorted(map(str, nums), key=cmp_to_key(lambda x,y: int(y+x)-int(x+y)))) if any(num>0 for num in nums) else "0"