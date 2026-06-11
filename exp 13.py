def climb_stairs(n):
    if n <= 2:
        return n

    a, b = 1, 2

    for i in range(3, n + 1):
        a, b = b, a + b

    return b


n = int(input("Enter number of steps: "))
print("Ways to climb:", climb_stairs(n))
