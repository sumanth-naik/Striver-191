class Solution:
    def restoreIpAddresses(self, s):
        validIpAddresses, n = set(), len(s)
        def recursion(indexArr):
            if len(indexArr)==5 and indexArr[-1]==n:
                validIpAddresses.add('.'.join([s[indexArr[i]:indexArr[i+1]] for i in range(4)]))
                return
            if indexArr[-1]<n:
                recursion(indexArr + [indexArr[-1]+1])
            if indexArr[-1]<n-1 and 10<=int(s[indexArr[-1]:indexArr[-1]+2])<=99:
                recursion(indexArr + [indexArr[-1]+2])
            if indexArr[-1]<n-2 and 100<=int(s[indexArr[-1]:indexArr[-1]+3])<=255:
                recursion(indexArr + [indexArr[-1]+3])
        recursion([0])
        return validIpAddresses