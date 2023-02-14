class Solution:
    def say(self, s):
        ansArr, curr, count = [], s[0], 0
        for ch in s:
            if ch!=curr:
                ansArr += [str(count),curr]
                curr, count = ch, 0
            count += 1
        ansArr += [str(count),curr]
        return ''.join(ansArr)

    def countAndSay(self, n):
        if n==1: return "1"
        return self.say(self.countAndSay(n-1))