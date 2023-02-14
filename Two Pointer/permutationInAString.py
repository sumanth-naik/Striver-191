from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str):
        need = Counter(s1)
        left, right, n = 0, 0, len(s2)
        while right<n:
            if s2[right] not in need:
                right += 1
                left = right
                need = Counter(s1)
            else:
                if need[s2[right]]==0:
                    while left<=right and s2[left]!=s2[right]:
                        if s2[left] in need:
                            need[s2[left]] += 1
                        left += 1
                    left += 1
                else:
                    need[s2[right]] -= 1
                    if sum(need.values())==0:
                        return True
                right += 1
        return False