class Solution:
    def intToRoman(self, num: int) -> str:
        mapper = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", \
        10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC",\
        100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM",\
        1000:"M", 2000:"MM", 3000:"MMM"}

        num, ans = str(num), ""
        n = len(num)
        return ''.join(mapper[int(num[index])*(10**(n-1-index))] for index in range(n) if num[index]!="0")


class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]