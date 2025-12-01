n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         dp[i][j] = float('-inf')
dp[0][0] = 1

for i in range(n):
    for j in range(m):

        for k in range(i):
            for l in range(j):

                if dp[k][l] == 0:
                    continue
                
                if grid[k][l] < grid[i][j]:
                    dp[i][j] = max(dp[i][j], dp[k][l] + 1)

ans = float('-inf')

for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])

print(ans)