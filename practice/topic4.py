def fib_memo( n, memo=None):
    if memo is None:
        memo = {}

    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fib_memo(n-1, memo)+  fib_memo(n-2, memo)
    return memo[n]

print(fib_memo(50))

def fib_tab(n):
    if n <= 1:
        return n
    
    dp_table = [0] * (n+1)

    dp_table[1] = 1

    for i in range (2, n + 1):
        dp_table[i] = dp_table[i-1] + dp_table[i-2]
    return dp_table[n]
print(fib_tab(50))