from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str):
        need = Counter(p)
        left, right, n = 0, 0, len(s)
        indices = []
        while right<n:
            if s[right] not in need:
                right += 1
                left = right
                need = Counter(p)
            else:
                if need[s[right]]==0:
                    while left<=right and s[left]!=s[right]:
                        if s[left] in need:
                            need[s[left]] += 1
                        left += 1
                    left += 1
                else:
                    need[s[right]] -= 1
                    if sum(need.values())==0:
                        indices.append(left)
                        need[s[left]] += 1
                        left += 1
                right += 1
        return indices


class Solution:
    def findAnagrams(self, s: str, p: str):
        lenOfS, lenOfP, hashOfS, hashOfP, indices, counterOfP = len(s), len(p), 0, 0, [], Counter(p)
        if lenOfP>lenOfS: return []
        for i in range(lenOfP):
            hashOfP += hash(p[i])
            hashOfS += hash(s[i])
        if hashOfS==hashOfP and Counter(s[0:lenOfP])==counterOfP: indices.append(0)
        for i in range(lenOfP, lenOfS):
            hashOfS = hashOfS + hash(s[i]) - hash(s[i-lenOfP])
            if hashOfS==hashOfP and Counter(s[i+1:i+lenOfP+1])==counterOfP: indices.append(i-lenOfP+1)
        return indices