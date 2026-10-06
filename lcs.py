def lcs(X, Y):
    m = len(X)
    n = len(Y)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n], dp


def build_lcs(X, Y, dp):
    i = len(X)
    j = len(Y)

    result = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            result.insert(0, X[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return result


X = input("Enter first string: ")
Y = input("Enter second string: ")

length, dp = lcs(X, Y)

result = build_lcs(X, Y, dp)

print("Length of LCS:", length)
print("LCS:", "".join(result))
