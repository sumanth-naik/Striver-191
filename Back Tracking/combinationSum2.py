class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        def backtracking(currentIndex, currentCombination, sumLeft):
            nonlocal combinations
            if sumLeft==0:
                combinations.append(deepcopy(currentCombination))
            else:
                prevNum = -1
                for index in range(currentIndex, len(candidates)):
                    if candidates[index]==prevNum:
                        continue
                    else:
                        if candidates[index]<=sumLeft:
                            currentCombination.append(candidates[index])
                            backtracking(index+1, currentCombination, sumLeft-candidates[index])
                            currentCombination.pop()
                            prevNum = candidates[index]
                        else:
                            break
        backtracking(0, [], target)
        return combinations
    
import bisect
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        def backtracking(currentIndex, currentCombination, sumLeft):
            nonlocal combinations
            if sumLeft==0:
                combinations.append(deepcopy(currentCombination))
            else:
                index = currentIndex
                while index<len(candidates):
                    if candidates[index]<=sumLeft:
                        currentCombination.append(candidates[index])
                        backtracking(index+1, currentCombination, sumLeft-candidates[index])
                        currentCombination.pop()
                        index = bisect.bisect_right(candidates, candidates[index])
                    else:
                        break
        backtracking(0, [], target)
        return combinations