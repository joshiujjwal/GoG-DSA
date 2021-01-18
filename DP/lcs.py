def lcs(s1, s2, m , n, memo):
    if memo[m][n] != -1:
        return memo[m][n]

    if m == 0 or n == 0:
        memo[m][n] = 0
    else:
        if s1[m-1] == s2[n-1]:
            memo[m][n]  =  1 + lcs(s1,s2,m-1,n-1,memo)
        else:
            memo[m][n]  =  max(lcs(s1,s2,m-1,n,memo), lcs(s1,s2,m,n-1,memo))
    return memo[m][n]

if __name__ == "__main__":
    s1 = "ABXY"
    s2 = "ABY"
    m = 4
    n = 3
    memo = [[-1] * (n+1) for _ in range(0,m+1)]
    print(lcs(s1, s2, m, n, memo))