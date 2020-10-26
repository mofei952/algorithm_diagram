word_a = 'fish'
word_b = 'fosh'

dp = [[0] * len(word_b) for _ in range(len(word_a))]

for i in range(len(word_a)):
    for j in range(len(word_b)):
        if word_a[i] == word_b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


for row in dp:
    print(row)
