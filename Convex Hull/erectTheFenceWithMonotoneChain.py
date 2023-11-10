# Key Idea: Monotone Chain: -> Sort so that you only deal with points going from left to right, thus slopes in Q1, Q4
#                           -> For contructing upper hull, pop when later slope is higher; For lower, opposite

# Note 1: Dont divide for getting slopes, just rearrange
# Note 2: points can be both upper and lower, so use set.

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
       
        def getOrientation(p1, p2, p3):
            x1, y1 = p1 
            x2, y2 = p2 
            x3, y3 = p3 
            return ((y3 - y2)*(x2 - x1) - (y2 - y1)*(x3 - x2)) # Note 1
        
        upper, lower = [], []
        for point in map(tuple, sorted(trees)):
            while len(upper)>=2 and getOrientation(upper[-2], upper[-1], point)>0:
                upper.pop()
            while len(lower)>=2 and getOrientation(lower[-2], lower[-1], point)<0:
                lower.pop()
            upper.append(point)
            lower.append(point)
            
        return list(set(upper+lower)) # Note
  