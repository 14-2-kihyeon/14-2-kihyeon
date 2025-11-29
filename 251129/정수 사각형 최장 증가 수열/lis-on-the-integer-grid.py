n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


cell = []

for i in range(n):
    for j in range(n):
        cell.append([grid[i][j], i, j])

cell.sort()

dp = [[1] * (n) for _ in range(n)]

dis,djs = [0, 1, 0, -1], [1, 0, -1, 0]

for _, x, y in cell:

    for di, dj, in zip(dis, djs):
        ni, nj = x + di, y + dj
        if ni < 0 or nj < 0 or ni >= n or nj >= n: continue
        if grid[ni][nj] > grid[x][y]:
            dp[ni][nj] = max(dp[x][y] + 1, dp[ni][nj])

ans = float('-inf')

for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])

print(ans)