import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def push(new_arr):

    for row in new_arr:
        tmp1 = []
        for i in range(n-1, -1, -1):
            if row[i] != 0:
                tmp1.append(row[i])
        
        tmp2 = []
        i = 0
        while i < len(tmp1):
            if i+1 < len(tmp1) and tmp1[i] == tmp1[i+1]:
                tmp2.append(tmp1[i]*2)
                i += 2
            else:
                tmp2.append(tmp1[i])
                i += 1
        
        for i in range(n):
            row[i] = 0
        
        j = n - 1
        for num in tmp2:
            if j < 0:
                break
            row[j] = num
            j -= 1
    
    return new_arr




def dfs(lev, now_arr):
    global ans
    if lev == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, now_arr[i][j])
        return
    
    new_arr = [row[:] for row in now_arr]
    dfs(lev+1, push(new_arr))


    new_arr = [row[:] for row in now_arr]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = now_arr[n-1-j][i]
    dfs(lev+1, push(new_arr))


    new_arr = [row[:] for row in now_arr]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = now_arr[n-1-i][n-1-j]
    dfs(lev+1, push(new_arr))

    new_arr = [row[:] for row in now_arr]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = now_arr[j][n-1-i]
    dfs(lev+1, push(new_arr))



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


ans = float('-inf')
dfs(0, arr)

print(ans)
