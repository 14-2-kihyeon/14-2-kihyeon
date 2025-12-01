n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp = [[0] * (m) for _ in range(n)]
dp[0][0] = 1


for i in range(n):
    for j in range(m):

        if i <= n-1 and j <= n-1:
            for a in range(i+1, n):
                for b in range(j+1, m):
                    if grid[i][j] >= grid[a][b]: continue

                    dp[a][b] = max(dp[a][b], dp[i][j] + 1)



ans = float('-inf')

for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])

print(ans)