def calculate_levenshtein_distance(word1, word2) -> int:
    prev = [0] * (len(word2) + 1)

    for i in range(len(prev)):
        prev[i] = i

    for r in range(1, len(word1) + 1):
        curr = [0] * (len(word2) + 1)
        curr[0] = r

        for c in range(1, len(word2) + 1):
            if word1[r - 1] == word2[c - 1]:
                curr[c] = prev[c - 1]

            else:
                curr[c] = 1 + min(curr[c - 1], prev[c], prev[c - 1])
        prev = curr.copy()
    return prev[-1]
