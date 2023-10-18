class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lenOfWord, m, n = len(word), len(board), len(board[0])
        charToIndicesMap = defaultdict(list)
        for i in range(m):
            for j in range(n):
                charToIndicesMap[board[i][j]].append((i,j))

        # prune 1 -> not enough chars
        counter = Counter(word)
        if any(char not in charToIndicesMap or len(charToIndicesMap[char])<counter[char] for char in counter): 
            return False

        # prune 2 -> if prefix is longer than suffix, reverse (Ex: aaaaabcc)
        prefixIndex, suffixIndex = 0, lenOfWord-1
        while prefixIndex<lenOfWord and word[prefixIndex]==word[0]: prefixIndex += 1
        while suffixIndex>=0 and word[suffixIndex]==word[lenOfWord-1]: suffixIndex -= 1
        if lenOfWord-1-suffixIndex<prefixIndex: 
            word = word[::-1]
                    
        def findWord(i, j, wordIndex, visited):
            if wordIndex==lenOfWord: return True
            for di, dj in [[1,0],[0,1],[0,-1],[-1,0]]:
                newI, newJ = i+di, j+dj
                if 0<=newI<m and 0<=newJ<n and board[newI][newJ]==word[wordIndex] and (newI, newJ) not in visited:
                    visited.add((newI, newJ))
                    if findWord(newI, newJ, wordIndex+1, visited):
                        return True
                    visited.remove((newI, newJ))    
            return False

        if any(findWord(i, j, 1, set([(i, j)])) for i,j in charToIndicesMap[word[0]]): return True
        return False
        
    