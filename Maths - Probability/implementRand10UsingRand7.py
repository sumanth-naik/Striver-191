# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        def round1():
            rand = rand7()
            while rand==7: # retry
                rand = rand7()
            return 0 if rand in [1,2,3] else 5
        
        def round2():
            rand = rand7()
            while rand in [6,7]:
                rand = rand7()
            return rand
        
        return round1() + round2()

class Solution:
    def rand10(self):
        while True:
            rand = (rand7()-1)*7 + rand7()
            if rand<=40: return rand%10 + 1
        
        
