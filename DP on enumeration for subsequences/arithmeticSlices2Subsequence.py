# Key Idea 1: dp[index][delta] + 1, tells us in how many sequences can index'th element be the penultimate number
# nums[index]+delta (possible next in sequence) will have dp[index][delta] + 1 sequences where nums[index] is the penultimate number.
'''
7 7 7 7 7 [all store delta 0]
index 0 -> 0 
index 1 -> 1 (value = dp[0][0] + 1) {01} -> indices
index 2 -> 3 (value = dp[0][0] + 1 + dp[1][0] + 1) {02,   012, 12} -> indices
index 3 -> 7 (value = dp[0][0] + 1 + dp[1][0] + 1 + dp[2][0] + 1) {03,   013, 13,   023, 0123, 123, 23}
index 4 -> 15 (value = dp[0][0] + 1 + ... + dp[3][0] + 1) {04,   014, 14,   024, 0124, 124, 24,   034, 0134, 134, 0234, 01234, 1234, 234, 34 }
'''
# Key Idea 2: count the arithmetic slices as dp[left][delta](which is the number of contributions) if prev has dp[left][delta]>0

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n, count = len(nums), 0
        dp = [defaultdict(int) for _ in range(n)]

        for right in range(1, n):
            for left in range(right):
                delta = nums[right]-nums[left]
                dp[right][delta] += 1 + dp[left][delta]
                count += dp[left][delta]
                
        return count


# Key Idea 1: What all future numbers can current number contribute to?
# Key Idea 2a: Handle adding 3-lengthed sequences 
# Key Idea 2b: and >3 lengthed sequences separately

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        used, unused = Counter(), Counter(nums)
        numsWithSequences, count = defaultdict(Counter), 0
        # numsWithSequences[num] stores a map of delta to count
        # numsWithSequences[10] = {1: 2} -> indicates that the next 10 you will encounter will have
        # 2 sequences ending with delta 1 (like in 8,8,9,10 or 8,9,9,10)

        for num in nums:
            if num in numsWithSequences:
                count += sum(numsWithSequences[num].values())
                # Key Idea 2b
                # If we are here, then num has sequences of length atleast 3 where num is the ending number
                # Next logic adds >3 lengthed sequences since current num will be penultimate number in the resulting sequences and already seqLen>=3
                # Ex: if num = 10 and it had 2 sequences of delta 1 (like in 8, 8, 9, 10, 11)
                # 11 (possibleNext) will have 2 sequences of length 3+1 (first_8, 9, 10, 11 and second_8, 9, 10, 11)
                # Note that (9, 10, 11) is a 3-lengthed sequence and will be added by the other block of code
                for delta in numsWithSequences[num]:
                    possibleNext = num + delta
                    if unused[possibleNext]:
                        numsWithSequences[possibleNext][delta] += numsWithSequences[num][delta] 

            # Key Idea 2a
            # Adds any newly addable sequence => Adds if current element can be middle of two numbers, one in used and other in unused
            # Ex: unused counter has {10:3} and used has {8:2} and current num is 9 [like in 8,8,9,10,10,10]
            # every future 10 will have 2 3-lengthed arithmetic sequences via 9 (first_8,9,10 and second_8,9,10).
            for prev in used:
                delta = num - prev
                possibleNext = num + delta
                if unused[possibleNext]:
                    numsWithSequences[possibleNext][delta] += used[prev]
            
            used[num] += 1
            unused[num] -= 1
        
        return count


'''
Comparing both approaches
They are more similar than one may think

Ex: 8,8,9,10

When at num 9,

In first approach, we add '1 +' to indicate a 2-lengthed sequence ending at 9 that can be used by 10 to create a 3-lenghted sequence. 
That '1 +' gets triggered once for each of the 8s (i.e., when left = 0 and 1), thus making dp[9's index][1] = 2

In second appraoch, we optimise that part by adding used[8] which adds 2 directly

Also, adding dp[left][delta] in Approach 1 is analogous to adding numsWithSequences[num][delta] in Approach 2. Both add >3 lengthed sequences.

Essentially, instead of dp[index of each number] we started using numsWithSequences[number] to add each number's contribution in one shot.
'''



# Key Idea: Just count all the >=2 lengthed sequences. Remove them at the end like PIE.

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n, dp = len(nums), [defaultdict(int) for _ in range(len(nums))]

        for right in range(1, n):
            for left in range(right):
                delta = nums[right]-nums[left]
                dp[right][delta] += 1 + dp[left][delta]

        return sum(map(lambda x: sum(x.values()), dp)) - (n*(n-1))//2