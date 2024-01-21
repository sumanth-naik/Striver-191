# Key Idea 1: Start from target. Its like a tree. Find parent from a node
# Key Idea 2: Use Euclidean GCD-like logic to decrease x, y

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx>sx and ty>sy:
            tx, ty = (tx, ty%tx) if ty>tx else (tx%ty, ty)
        return (tx==sx and ty>=sy and not (ty-sy)%tx) or (ty==sy and tx>=sx and not (tx-sx)%ty)
