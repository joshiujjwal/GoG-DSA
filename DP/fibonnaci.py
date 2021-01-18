def fib(n, memo):
    if memo[n] == -1:
        res = 0
        if n == 1 or n == 0:
            res = n
        else:
            res = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = res
    return memo[n]

if __name__ == "__main__":
    n = 5
    memo = [-1] * (n + 1)
    print(fib(n, memo))



