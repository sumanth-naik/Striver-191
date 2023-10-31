# Key Idea: Take 3^7 example, figure out how to update n, m, res
# 3^7 -> 3 * 9^3 -> 3 * 9 * 9^2 -> 3 * 9 * 81^1 -> 3 * 9 * 81

def powMod(n, m, MOD):
    res = 1
    while m:
        if m&1:
            res = res * n % MOD
        n = n * n % MOD
        m //= 2
    return res