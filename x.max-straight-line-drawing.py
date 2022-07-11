ans = 0
grid =  [ 
		[0,1,0,0,0],
		[0,1,0,0,0],
		[1,1,1,0,0],
		[0,1,1,0,0],
		[0,1,0,1,0],
		[0,1,1,1,1]
	]

m = len(grid)
n = len(grid[0])

# 0 -> Bottom; 1 -> Right; 2-> Right diagonal; 3-> Left Diagonal
dp = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(m)]

for i in range(m-1, -1, -1):
	for j in range(n-1, -1, -1):
		if grid[i][j] == 1:
            
      # At least one is possible
			for k in range(4):
				dp[i][j][k] = 1
            
      # Case for bottom
			if i+1 < m:
				dp[i][j][0] += dp[i+1][j][0]
            
      # Case for right
			if j+1 < n:
				dp[i][j][1] += dp[i][j+1][1]
            
      # Case for right diagonal
			if i+1 < m and j+1 < n:
				dp[i][j][2] += dp[i+1][j+1][2]
                
      # Case for left diagonal
			if i+1 < m and j-1 >= 0:	
				dp[i][j][3] += dp[i+1][j-1][3]
            
      # This is storing the max ever from the 4 vals
			ans = max(ans, max(dp[i][j]))
            
for rows in dp:
    print(rows)

print(ans) 