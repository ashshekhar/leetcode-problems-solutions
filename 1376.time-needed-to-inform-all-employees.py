#
# @lc app=leetcode id=1376 lang=python
#
# [1376] Time Needed to Inform All Employees
#

# @lc code=start
class Solution(object):

    def dfs(self, res, time, node, visited, manager_to_subordinate):
        
        # Base case: Only inform time stores
        if not len(manager_to_subordinate):
            return 0

        # Base case
        if len(manager_to_subordinate[node]) == 1:
            return time

        time += manager_to_subordinate[node][0]

        for subordinates in manager_to_subordinate[node][1:]:
            if subordinates not in visited:
                visited.add(subordinates)
                
                # For each stage, you need to store the max ever encountered
                res = max(res, self.dfs(res, time, subordinates, visited, manager_to_subordinate))
        
        return res

    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        # Key is n value of the employee, value is (time to infrom, [list of subordinates])
        # Use of backtracking - Similar to course schedule
        manager_to_subordinate = {}
        
        # time = 0
        visited = set()
        
        # Creating dictionary mapping
        for subordinate, manager in enumerate(manager):
            if manager == -1:
                continue
                
            if manager not in manager_to_subordinate:
                manager_to_subordinate[manager] = [informTime[manager]]
                
            manager_to_subordinate[manager].append(subordinate)
            
            # For the rest of the subordinates
            if subordinate not in manager_to_subordinate:
                manager_to_subordinate[subordinate] = [informTime[subordinate]]
                
        res = self.dfs(0, 0, headID, visited, manager_to_subordinate)
            
        return res 
# @lc code=end