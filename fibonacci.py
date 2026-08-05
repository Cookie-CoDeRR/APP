def fibonacci_memoization(num, cache=None):
    if cache is None:
        cache = {}

    if num in cache:
        return cache[num]

    if num <= 1:
        return num

    cache[num] = fibonacci_memoization(num - 1, cache) + fibonacci_memoization(num - 2, cache)
    return cache[num]


def fibonacci_tabulation(num):
    if num <= 1:
        return num

    table = [0] * (num + 1)
    table[1] = 1

    for i in range(2, num + 1):
        table[i] = table[i - 1] + table[i - 2]

    print("Fibonacci Sequence (Tabulation):", table)
    return table[num]


def fibonacci_optimized(num):
    if num <= 1:
        return num

    prev, curr = 0, 1
    for _ in range(2, num + 1):
        prev, curr = curr, prev + curr
    return curr


n = int(input("Enter Fibonacci Position: "))

memo_result = fibonacci_memoization(n)
tab_result = fibonacci_tabulation(n)
opt_result = fibonacci_optimized(n)

print("\nResult using Memoization :", memo_result)
print("Result using Tabulation  :", tab_result)
print("Result using Optimized DP:", opt_result)
