#
# @lc app=leetcode id=547 lang=python
#
# [547] Number of Provinces
#

# @lc code=start
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        count = 0
        visited = set()
        
        # Prepare adj list
        adj_list = {i : [] for i in range(len(isConnected))}
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)

        # Return 1 if connected else 0
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            
            for neighbors in adj_list[node]:
                dfs(neighbors)
                
        # Visit the graph and only increment count for unvisited ndoes
        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                
            dfs(i)
            
        return count
        
# @lc code=end
