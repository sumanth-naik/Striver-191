# Key Idea 1: Separate wrt ending characters. 
# Key Idea 2: If we add current char to all the subsequences so far, 
#             any existing subsequence that ends with current char will be a duplicate 
# Key Idea 3: Need to add single curr char separately            


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        endsCount, countTillPrev = [0]*26, 0
        for char in s:
            index = ord(char) - ord('a')
            countTillPrev, endsCount[index] = 2*countTillPrev - endsCount[index] + 1, countTillPrev + 1
        return countTillPrev%(10**9+7)

'''
        abc ->
        a
        ab;  a;  b
        abc,ac,bc;  ab,a,b;  c

        lee ->
        l
        le;  l;  e
        lee,le,ee;  l;  e

        abaab ->
        a 
        ab;  b;  a 
        aba,ba,aa;  ab,b;  a
        abaa,baa,aaa,aba,ba,aa;  ab,b;  a
        abaab,baab,aaab,abab,bab,aab,abb,bb,ab;  abaa,baa,aaa,aba,ba,aa,a;  b
        
'''