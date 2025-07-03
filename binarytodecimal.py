n = "101"
decimal = 0
power = 0
for i in reversed(n):
    decimal += int(i) * (2 ** power)
    power += 1
print("Decimal value of", n, "is", decimal)