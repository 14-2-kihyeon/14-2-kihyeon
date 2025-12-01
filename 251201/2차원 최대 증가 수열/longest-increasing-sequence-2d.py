import sys

# INT_MIN을 사용하여 최댓값을 쉽게 찾을 수 있도록 합니다.
INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
# N: 행의 수, M: 열의 수
n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# DP 배열 정의: dp[i][j] = (i, j)에 도착했을 때 밟을 수 있는 최대 칸 수
# N x M 크기로 초기화합니다.
dp = [
    [0] * m
    for _ in range(n)
]

# 초기 조건: 시작점 (0, 0)은 1칸을 밟은 상태입니다.
dp[0][0] = 1


for i in range(n):
    for j in range(m):

        if dp[i][j] == 0:
            continue
            
        for a in range(i, n):
            for b in range(j, m):
                

                if a == i and b == j:
                    continue
                

                if grid[i][j] < grid[a][b]:
                    dp[a][b] = max(dp[a][b], dp[i][j] + 1)


ans = INT_MIN
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])


print(ans)