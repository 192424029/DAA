def champagne_tower(poured, query_row, query_glass):
    dp = [[0.0] * (k + 1) for k in range(101)]

    dp[0][0] = poured

    for r in range(query_row + 1):
        for c in range(r + 1):
            excess = (dp[r][c] - 1.0) / 2.0

            if excess > 0:
                dp[r + 1][c] += excess
                dp[r + 1][c + 1] += excess

    return min(1, dp[query_row][query_glass])


poured = int(input("Enter poured cups: "))
row = int(input("Enter query row: "))
glass = int(input("Enter query glass: "))

print("Glass filled:", champagne_tower(poured, row, glass))
