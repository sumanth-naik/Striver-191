class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        '''
        _ _ _ _ _ -> n=4, k=2 => in stars and bars, bars are identical, think of a setting making them identical
                  -> You will have to put 2 bars for each segment, making each bar identical
        | _ | | | -> (0,2),(2,3)
        | | | _ | -> (0,1),(1,3)
        | | _ | | -> (0,1),(2,3)
        _ | | | | -> (1,2),(2,3)
        | | | | _ -> (0,1),(1,2)

        '''
        return comb(n+k-1, 2*k)%(10**9+7)