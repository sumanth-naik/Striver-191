class Solution:
    def diffWaysToCompute(self, expression):
        symbols = ["+","-","*"]
        @lru_cache(None)
        def memoization(expressionString):
            if expressionString.isdigit():
                return [int(expressionString)]
            
            possibleEvaluations = []
            for i, char in enumerate(expressionString):
                if char in symbols:
                    leftSubtreePossibleEvalations = memoization(expressionString[:i])
                    rightSubtreePossibleEvalations = memoization(expressionString[i+1:])
                    for leftVal in leftSubtreePossibleEvalations:
                        for rightVal in rightSubtreePossibleEvalations:
                            if char=="+": possibleEvaluations.append(leftVal+rightVal)
                            if char=="-": possibleEvaluations.append(leftVal-rightVal)
                            if char=="*": possibleEvaluations.append(leftVal*rightVal)
            return possibleEvaluations
        return memoization(expression)
