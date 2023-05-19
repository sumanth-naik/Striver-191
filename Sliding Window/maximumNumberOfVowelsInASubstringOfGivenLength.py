class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        maxCount = count = sum(char in vowels for char in s[:k])
        left, right = 0, k
        while right<len(s):
            count += ((s[right] in vowels) - (s[left] in vowels))
            left+=1
            right+=1
            maxCount = max(maxCount, count)
        return maxCount
    
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a","e","i","o","u"}
        maxCount = count = sum(char in vowels for char in s[:k])
        for right in range(k, len(s)):
            count += ((s[right] in vowels) - (s[right-k] in vowels))
            maxCount = max(maxCount, count)
        return maxCount