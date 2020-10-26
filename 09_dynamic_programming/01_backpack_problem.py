goods = ['A', 'B', 'C', 'D']
values = [1500, 3000, 2000, 2000]
weights = [1, 4, 3, 1]
backpack_weight = 4

dp = [[0] * backpack_weight for _ in range(len(goods))]


for i in range(len(goods)):
    for j in range(backpack_weight):
        current_backpack_weight = j + 1
        current_goods_weight = weights[i]

        value1 = 0
        if current_backpack_weight >= current_goods_weight:
            value0 = dp[i-1][j-current_goods_weight] if i > 0 and j - \
                current_goods_weight >= 0 else 0
            value1 = values[i] + value0

        value2 = dp[i-1][j] if i > 0 else 0

        dp[i][j] = max(value1, value2)

for row in dp:
    print(row)
