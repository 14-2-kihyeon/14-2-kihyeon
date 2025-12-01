n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

dp = [0] * (1001)


for i in range(n): # n = 3  i = 0, 1, 2
    dp[arr[i][0]] = 1       
    for j in range(i):
        if arr[i][0] > arr[j][1]:
            dp[arr[i][0]] = max(dp[arr[i][0]], dp[arr[j][0]] + 1)

print(max(dp)) 
         
    
    

