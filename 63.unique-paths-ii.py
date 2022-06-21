#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # If initially blocked, return, else mark that as 1 number of ways to reach
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            obstacleGrid[0][0] = 1
        
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])   

        # Only if the prev cell is visitable (== 1) and current is (== 0) allowed to be visited, set it as 1 else 0
        for i in range(1, row):
            obstacleGrid[i][0] = int(obstacleGrid[i-1][0] == 1 and obstacleGrid[i][0] == 0)

        for j in range(1, col):
            obstacleGrid[0][j] = int(obstacleGrid[0][j-1] == 1 and obstacleGrid[0][j] == 0)
        
        # Finally, if you see a visitable cell, update its value else set it to 0, that is can't be visited or can be visited in 0 ways
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = 0

        return obstacleGrid[row-1][col-1]
# @lc code=end

