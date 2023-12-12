# Key Idea 1: Separate wrt ending characters. 
# Key Idea 2: If we add current char to all the subsequences so far, 
#             any existing subsequence that ends with current char will be a duplicate 
# Key Idea 3: Need to add single curr char separately   
# Key Idea 4: Iterate in reverse to make life easier         


class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        endsWithZero, endsWithOne = 0, 0
        for char in binary[::-1]:
            if char=='0':
                endsWithZero += endsWithOne + 1
            else:
                endsWithOne += endsWithZero + 1

        return (endsWithOne + int(endsWithZero>0))%(10**9 + 7)

# concise
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        endsWith = [0, 0]
        for char in reversed(binary):
            endsWith[int(char)] += endsWith[1-int(char)] + 1
            # Key Idea 2: same as: endsWith[int(char)] = sum(endsWith) - endsWith[int(char)] + 1
        return (endsWith[1] + int(endsWith[0]>0))%(10**9 + 7)


# Iterating left to right -> trickier
# Key Idea: Add "0" only at the end, if possible

class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        endsWithZero, endsWithOne, hasZero = 0, 0, False
        for char in binary:
            if char=='0':
                endsWithZero += endsWithOne
                hasZero = True
            else:
                endsWithOne += endsWithZero + 1

        return (endsWithZero + endsWithOne + int(hasZero))%(10**9 + 7)

'''
001
0; 
0; 
0; 01,1


101 10

; 1
0,10; 1
0,10; 101; 11; 1


1,0,10,11,01,101 -> 0,10; 1,11,01,101
0,10; 01,101; 11,111,011,1011; 1

0,100; 010,1010,110,1110,0110,10110,10; 01,101,11,111,011,1011,1


{xyz}1 {abc}0 -> add 1 -> 
{abc}01 -> {xyz}1 [Every one]
{xyz}11 -> {xyz}1   

'''