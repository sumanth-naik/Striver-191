def isPalindrome(s,i,j):
    if i>=j:
        return True
    return s[i]==s[j] and isPalindrome(s,i+1,j-1)

def longestPalindrome(s):
    n = len(s)
    longestPalindrome = (0,0)
    for i in range(n):
        for j in range(i,n):
            if isPalindrome(s, i, j) and longestPalindrome[1] - longestPalindrome[0] <j-i:
                longestPalindrome = (i,j)
                
    return s[longestPalindrome[0]:longestPalindrome[1]+1]
                
s = "cbbd"
#print(longestPalindrome(s))






def isPalindrome(s,i,j, dp):
    if i>=len(s) or j<0:
        return True
    if dp[i][j] == -1:
        if i>=j:
            dp[i][j] = True
        else:
            dp[i][j] = s[i]==s[j] and isPalindrome(s,i+1,j-1,dp)
    
    return dp[i][j]

def longestPalindromeWithMemo(s):
    n = len(s)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    longestPalindrome = (0,0)
    for i in range(n):
        for j in range(i,n):
            if isPalindrome(s, i, j, dp) and longestPalindrome[1] - longestPalindrome[0] <j-i:
                longestPalindrome = (i,j)
                
    return s[longestPalindrome[0]:longestPalindrome[1]+1]
                
s = "cbbd"
s="vvgogaewginhopuxzwyryobjjpieyhwfopiowxmyylvcgsnhfcnogpqpukzmnpewavoutbloyrrhatimmxfqmcwgfebuoqbbgvubbkjfvxivjfijlpvtsnhagzfptahhyojwzamayoiegkenycnkxzkambimhdykdcxyyfjnvztzypmfczdhhnkmfuvgkhzbwmjznykkagqdrueohgcmeidjqsvfugcioeduohprjtfdmtzosnhoiganffarokxjifzzxhixdzycwfheqqegduzwtiacmdhqfmxhazcxsqyrvrihfqzjxvawdeandnwgjlquvzadruiqmcsgibglhicsvzqknztqpkiihdoisxipkourentfvrltieihiktgzswtgcmmlfrjifqinhrbplbsgswqlbjkyxjwoshsvxlhlpgzwbmxzwaemtowcxwourjwmmwjruowxcwotmeawzxmbwzgplhlxvshsowjxykjblqwsgsblpbrhniqfijrflmmcgtwszgtkihieitlrvftneruokpixsiodhiikpqtznkqzvscihlgbigscmqiurdazvuqljgwndnaedwavxjzqfhirvryqsxczahxmfqhdmcaitwzudgeqqehfwcyzdxihxzzfijxkoraffnagiohnsoztmdftjrphoudeoicgufvsqjdiemcghoeurdqgakkynzjmwbzhkgvufmknhhdzcfmpyztzvnjfyyxcdkydhmibmakzxkncynekgeioyamazwjoyhhatpfzgahnstvpljifjvixvfjkbbuvgbbqoubefgwcmqfxmmitahrryolbtuovawepnmzkupqpgoncfhnsgcvlyymxwoipofwhyeipjjboyrywzxupohnigweagogvv"
#print(longestPalindromeWithMemo(s))






def longestPalindromeTabulation(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0,n-1):
        dp[i][i] = 1
        dp[i+1][i] = 1
    dp[n-1][n-1] = 1
    
    longestPalindrome = (0,0)

    for diffInIAndJ in range(1,n):
        for row in range(0,n-diffInIAndJ):
            if s[row]==s[row+diffInIAndJ] and dp[row+1][row+diffInIAndJ-1]:
               dp[row][row+diffInIAndJ] = 1
               
               if longestPalindrome[1] - longestPalindrome[0]<diffInIAndJ:
                   longestPalindrome = (row,row+diffInIAndJ)
            
                
    return s[longestPalindrome[0]:longestPalindrome[1]+1]
                
s = "cbbd"
s="vvgogaewginhopuxzwyryobjjpieyhwfopiowxmyylvcgsnhfcnogpqpukzmnpewavoutbloyrrhatimmxfqmcwgfebuoqbbgvubbkjfvxivjfijlpvtsnhagzfptahhyojwzamayoiegkenycnkxzkambimhdykdcxyyfjnvztzypmfczdhhnkmfuvgkhzbwmjznykkagqdrueohgcmeidjqsvfugcioeduohprjtfdmtzosnhoiganffarokxjifzzxhixdzycwfheqqegduzwtiacmdhqfmxhazcxsqyrvrihfqzjxvawdeandnwgjlquvzadruiqmcsgibglhicsvzqknztqpkiihdoisxipkourentfvrltieihiktgzswtgcmmlfrjifqinhrbplbsgswqlbjkyxjwoshsvxlhlpgzwbmxzwaemtowcxwourjwmmwjruowxcwotmeawzxmbwzgplhlxvshsowjxykjblqwsgsblpbrhniqfijrflmmcgtwszgtkihieitlrvftneruokpixsiodhiikpqtznkqzvscihlgbigscmqiurdazvuqljgwndnaedwavxjzqfhirvryqsxczahxmfqhdmcaitwzudgeqqehfwcyzdxihxzzfijxkoraffnagiohnsoztmdftjrphoudeoicgufvsqjdiemcghoeurdqgakkynzjmwbzhkgvufmknhhdzcfmpyztzvnjfyyxcdkydhmibmakzxkncynekgeioyamazwjoyhhatpfzgahnstvpljifjvixvfjkbbuvgbbqoubefgwcmqfxmmitahrryolbtuovawepnmzkupqpgoncfhnsgcvlyymxwoipofwhyeipjjboyrywzxupohnigweagogvv"
#print(longestPalindromeTabulation(s))





def longestPalindromeTabulationWithSpaceOptimization(s):
    n = len(s)
    dp1 = [1 for _ in range(n)]
    dp2 = [1 for _ in range(n)]
    dp3 = [0 for _ in range(n)]

    longestPalindrome = (0,0)

    for diffInIAndJ in range(1,n):
        for row in range(0,n-diffInIAndJ):
            if s[row]==s[row+diffInIAndJ] and dp1[row+diffInIAndJ-1]:
               dp3[row+diffInIAndJ] = 1
               
               if longestPalindrome[1] - longestPalindrome[0]<diffInIAndJ:
                   longestPalindrome = (row,row+diffInIAndJ)

        dp3,dp2,dp1 = [0 for _ in range(n)],dp3,dp2
                
    return s[longestPalindrome[0]:longestPalindrome[1]+1]
                
s = "cbbd"
s="thelviymgkeddreyviespjsyqwmbmnlwzjhdokfzrczvreiagayofwvhecskjqlqzodtozvzozqyiwfsjyrinrmgfyhplybonzuvmxxyihmggwiuccplqjtgschmieoexvtewbsjqzkzapfxpzhgjtbmlchevohmxnbattphvobptnhmcoihcaimchurqpucxapojgszpopdvsfahwidiyxlpjfhdkcoewzvlmaebudtovnvcuadykhhmwfpilqfdvnseiitokcbuxmhwukrdxwvtgztczrwcsydqwosnktronibiplbljrcpinqorbhxrwjonnqeniebrksjkcmbvjnuwdedoenqmrcxayqbzmlpbubnfnkkqnuljtchaeijcmfpyuxkgfssoqliqmhowtbmcvzkqbanxhowjjejexxlihwwhilxxejejjwohxnabqkzvcmbtwohmqilqossfgkxuypfmcjieahctjlunqkknfnbubplmzbqyaxcrmqneodedwunjvbmckjskrbeineqnnojwrxhbroqnipcrjlblpibinortknsowqdyscwrzctzgtvwxdrkuwhmxubckotiiesnvdfqlipfwmhhkydaucvnvotdubeamlvzweockdhfjplxyidiwhafsvdpopzsgjopaxcupqruhcmiachiocmhntpbovhpttabnxmhovehclmbtjghzpxfpazkzqjsbwetvxeoeimhcsgtjqlpccuiwggmhiyxxmvuznobylphyfgmrniryjsfwiyqzozvzotdozqlqjkscehvwfoyagaiervzcrzfkodhjzwlnmbmwqysjpseivyerddekgmyivleht"
print(longestPalindromeTabulationWithSpaceOptimization(s))



