def waystomakechange(amount, coins):
    def helper(n, i):
        if n == 0:
            return 1
        if n < 0 or i >= len(coins):
            return 0
        return helper(n, i + 1) + helper(n - coins[i], i)
    return helper(amount, 0)
coins = [1, 2, 5, 10]
amount = 2
result = waystomakechange(amount, coins)
print("Number of ways to make change for", amount, "is:", result)