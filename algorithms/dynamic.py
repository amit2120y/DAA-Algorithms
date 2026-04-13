def knapsack_dp(values, weights, W):
    n = len(values)
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(W+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w],
                               values[i-1] + dp[i-1][w-weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

def lcs(X, Y):
    n = len(X)
    m = len(Y)
    l = {}

    for i in range(n + 1):
        l[(i, 0)] = 0
    for j in range(m + 1):
        l[(0, j)] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                l[(i, j)] = l[(i - 1, j - 1)] + 1
            else:
                l[(i, j)] = max(l[(i - 1, j)], l[(i, j - 1)])

    lcs_sequence = []
    i, j = n, m
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_sequence.append(X[i - 1])
            i -= 1
            j -= 1
        elif l[(i - 1, j)] > l[(i, j - 1)]:
            i -= 1
        else:
            j -= 1

    lcs_sequence.reverse()
    return l[(n, m)], ''.join(lcs_sequence)

def matrix_chain_multiply(dimensions):
    n = len(dimensions) - 1
    dp = [[float('inf')] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dimensions[i] * dimensions[k+1] * dimensions[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k
    min_cost = int(dp[0][n-1]) if dp[0][n-1] != float('inf') else 0
    return min_cost, split