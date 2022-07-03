#
# @lc app=leetcode id=1553 lang=python
#
# [1553] Minimum Number of Days to Eat N Oranges
#

# @lc code=start
from collections import deque
class Solution(object):
    
    # DP Solution
    # def minDays(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     dp = {0: 0, 1: 1}

    #     def dfs(n):
    #         if n in dp:
    #             return dp[n]
            
    #         # This would obv be the longest
    #         # one = 1 + dfs(n - 1)
            
    #         # Instead, either go down / 2 path or -1 then /2
    #         two = 1 + (n % 2) + dfs(n // 2)
            
    #         # Or, either go down / 3 path or -1 then / 3
    #         three = 1 + (n % 3) + dfs(n // 3)
            
    #         # Store the shortest
    #         dp[n] = min(two, three)

    #         return dp[n]
            
    #     return dfs(n)    
    
    # BFS Solution
    def minDays(self, n):
        q = deque([n])
        days = 0
        visited = set()
        
        while q:
            days += 1
            for _ in range(len(q)):
                node = q.popleft()
                
                # Base case
                if node == 1:
                    return days
                
                if node - 1 not in visited:
                    q.append(node - 1)
                    visited.add(node - 1)
                
                if node % 2 == 0 and node % 2 not in visited:
                    q.append(node // 2)
                    visited.add(node // 2)
                    
                if node % 3 == 0 and node % 3 not in visited:
                    q.append(node // 3)
                    visited.add(node // 3)
                
# @lc code=end

