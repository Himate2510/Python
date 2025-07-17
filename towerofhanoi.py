def Hanoi(n, a, b, c):
    if n == 1:
        print("Move disk 1 from", a, "to", c)
        return
    Hanoi(n - 1, a, c, b)
    print("Move disk", n, "from", a, "to", c)
    Hanoi(n - 1, b, a, c)
n = 4
Hanoi(n, 'A', 'B', 'C')