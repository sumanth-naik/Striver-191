s = "wsgdzojcrxtfqcfkhhcuxxnbwtxzkkeunmpdsqfvgfjhusholnwrhmzexhfqppatkexuzdllrbaxygmovqwfvmmbvuuctcwxhrmepxmnxlxdkyzfsqypuroxdczuilbjypnirljxfgpuhhgusflhalorkcvqfknnkqyprxlwmakqszsdqnfovptsgbppvejvukbxaybccxzeqcjhmnexlaafmycwopxntuisxcitxdbarsicvwrvjmxsapmhbbnuivzhkgcrshokkioagwidhmfzjwwywastecjsolxmhfnmgommkoimiwlgwxxdsxhuwwjhpxxgmeuzhdzmuqhmhnfwwokgvwsznfcoxbferdonrexzanpymxtfojodcfydedlxmxeffhwjeegqnagoqlwwdctbqnuxngrgovrjesrkjrfjawknbrsfywljscfvnjhczhyeoyzrtbkvvfvofykkwoiclgxyaddhpdoztdhcbauaagjmfzkkdqexkczfsztckdlujgqzjyuittnudpldjvsbwbzcsazjpxrwfafievenvuetzcxynnmskoytgznvqdlkhaowjtetveahpjguiowkiuvikwewmgxhgfjuzkgrkqhmxxavbriftadtogmhlatczusxkktcsyrnwjbeshifzbykqibghmmvecwwtwdcscikyzyiqlgwzycptlxiwfaigyhrlgtjocvajcnqyenxrnjgogeqtvkxllxpuoxargzgcsfwavwbnktchwjebvwwhfghqkcjhuhuqwcdsixrkfjxuzvhjxlyoxswdlwfytgbtqbeimzzogzrlovcdpseoafuxfmrhdswwictsctawjanvoafvzqanvhaohgndbsxlzuymvfflyswnkvpsvqezekeidadatsymbvgwobdrixisknqpehddjrsntkqpsfxictqbnedjmsveurvrtvpvzbengdijkfcogpcrvwyf"
s = "babad"
s="mqizdjrfqtmcsruvvlhdgzfrmxgmmbguroxcbhalzggxhzwfznfkrdwsvzhieqvsrbyedqxwmnvovvnesphgddoikfwuujrhxwcrbttfbmlayrlmpromlzwzrkjkzdvdkpqtbzszrngczvgspzpfnvwuifzjdrmwfadophxscxtbavrhfkadhxrmvlmofbzqshqxazzwjextdpuszwgrxirmmlqitjjpijptmqfbggkwaolpbdglmsvlwdummsrdyjhmgrasrblpjsrpkkgknsucsshjuxunqiouzrdwwooxclutkrujpfebjpoodvhknayilcxjrvnykfjhvsikjabsdnvgguoiyldshbsmsrrlwmkfmyjbbsylhrusubcglaemnurpuvlyyknbqelmkkyamrcmjbncpafchacckhymtasylyfjuribqxsekbjkgzrvzjmjkquxfwopsbjudggnfbuyyfizefgxamocxjgkwxidkgursrcsjwwyeiymoafgyjlhtcdkgrikzzlenqgtdukivvdsalepyvehaklejxxmmoycrtsvzugudwirgywvsxqapxyjedbdhvkkvrxxsgifcldkspgdnjnnzfalaslwqfylmzvbxuscatomnmgarkvuccblpoktlpnazyeazhfucmfpalbujhzbykdgcirnqivdwxnnuznrwdjslwdwgpvjehqcbtjljnxsebtqujhmteknbinrloregnphwhnfidfsqdtaexencwzszlpmxjicoduejjomqzsmrgdgvlrfcrbyfutidkryspmoyzlgfltclmhaeebfbunrwqytzhuxghxkfwtjrfyxavcjwnvbaydjnarrhiyjavlmfsstewtxrcifcllnugldnfyswnsewqwnvbgtatccfeqyjgqbnufwttaokibyrldhoniwqsflvlwnjmffoirzmoxqxunkuepj"

def lengthOfLongestPalindromeFromIndexI(index, s, reversedS):
    n = len(s)
    stringForKMP =  s[index:] + "#" + reversedS[:n-index] 
    #print(stringForKMP, index)
    lpsArr = [0 for _ in range(len(stringForKMP))]
    prevLpsLength = 0
    for i in range(1, len(stringForKMP)):
        while prevLpsLength!=0 and stringForKMP[prevLpsLength]!=stringForKMP[i]:
            prevLpsLength = lpsArr[prevLpsLength-1]
        if stringForKMP[prevLpsLength]!=stringForKMP[i]:
            lpsArr[i] = 0
        else:
            lpsArr[i] = prevLpsLength + 1
            prevLpsLength += 1
    #print(lpsArr)
    return lpsArr[len(stringForKMP)-1]

def longestPalindrome(s: str) -> str:

    reversedS = s[::-1]
    longestPalindrome = ""
    for index in range(len(s)):
        length = lengthOfLongestPalindromeFromIndexI(index, s, reversedS)
        if(len(longestPalindrome)<length):
            longestPalindrome = s[index:index+length]
        if(length==len(s)-index):
            return longestPalindrome
    return(longestPalindrome)
        
print(longestPalindrome(s))




def lengthOfLongestPalindromeFromIndex(index, combinedReverseString):
    n = len(combinedReverseString) - 2*index
    lpsArr = [0 for _ in range(n)]
    prevLpsLength = 0
    for i in range(1, n):
        #print(combinedReverseString[index+i],end="")
        while prevLpsLength!=0 and combinedReverseString[index+prevLpsLength]!=combinedReverseString[i+index]:
            prevLpsLength = lpsArr[prevLpsLength-1]
        if combinedReverseString[index+prevLpsLength]!=combinedReverseString[i+index]:
            lpsArr[i] = 0
        else:
            lpsArr[i] = prevLpsLength + 1
            prevLpsLength += 1
    #print("\n",combinedReverseString, index, lpsArr)
    return lpsArr[n-1]

def longestPalindrome2(s: str) -> str:

    combinedReverseString = s + "#" + s[::-1]
    longestPalindrome = ""
    for index in range(len(s)):
        length = lengthOfLongestPalindromeFromIndex(index, combinedReverseString)
        if(len(longestPalindrome)<length):
            longestPalindrome = s[index:index+length]
        if(length==len(s)-index):
            return longestPalindrome
    return(longestPalindrome)
        
print(longestPalindrome2(s))