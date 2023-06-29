from copy import deepcopy

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def backtracking(currIndex, currCombination, sumLeft):
            nonlocal combinations
            if sumLeft==0:
                combinations.append(deepcopy(currCombination))
            else:
                for index in range(currIndex, len(candidates)):
                    if sumLeft>=candidates[index]:
                        currCombination.append(candidates[index])
                        backtracking(index, currCombination, sumLeft-candidates[index])
                        currCombination.pop()
                    else:
                        break

        backtracking(0, [], target)
        
        return combinations
