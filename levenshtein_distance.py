def calculate_levenshtein_distance(word1, word2) -> int:
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    for i in range(len(word2) + 1):
        dp[0][i] = i

    for i in range(len(word1) + 1):
        dp[i][0] = i

    for r in range(1, len(word1) + 1):
        for c in range(1, len(word2) + 1):

            # Equal
            if word1[r - 1] == word2[c - 1]:
                dp[r][c] = dp[r - 1][c - 1]

            # Deletion, Insertion, Substitution
            else:
                dp[r][c] = 1 + min(dp[r][c - 1], dp[r - 1][c], dp[r - 1][c - 1])

            # Transposition
            if r > 1 and c > 1 and word1[r - 2] == word2[c - 1] and word1[r - 1] == word2[c - 2]:
                dp[r][c] = min(dp[r][c], dp[r - 2][c - 2] + 1)

    return dp[-1][-1]