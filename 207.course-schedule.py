#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start
class Solution(object):    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Graph problem
        prerequisiteMap = {i: [] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            prerequisiteMap[course].append(prereq)
        
        visit = set()
        
        def dfs(course):
            
            # Cycle
            if course in visit:
                return False
            
            if prerequisiteMap[course] == []:
                return True

            visit.add(course)
            
            for prereqs in prerequisiteMap[course]:
                if not dfs(prereqs): return False
            
            visit.remove(course)
            prerequisiteMap[course] = []
            
            return False
            
        for course in range(numCourses):
            if not dfs(course): return False
        
        return True
    
        
# @lc code=end

