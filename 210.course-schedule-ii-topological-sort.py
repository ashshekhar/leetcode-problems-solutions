#
# @lc app=leetcode id=210 lang=python
#
# [210] Course Schedule II
#

# @lc code=start
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        pre_dict = {i: [] for i in range(numCourses)}
        
        # Holds final topological sort
        global res
        res = []
        
        # For final ordering - Don't want to visit same course twice
        visited = set()
        
        # To detect loop in current iteration
        currently_visiting = set()
        
        for course in prerequisites:
            pre_dict[course[0]].append(course[1])
            
        
        def dfs(course):
            
            global res
            
            # Cycle detected on way to traverse a course
            if course in currently_visiting:
                return False
            
            # Already added in topological sort: return True since successfully visited
            if course in visited:
                return True
            
            # Add to current iteration
            currently_visiting.add(course)
            
            for prereqs in pre_dict[course]:
                if not dfs(prereqs):
                    return False
            
            # On reaching the last course in dfs, prereq would be []
            # So here we remove the last course from currently_visiting
            # And add it to finally visited and outptut.
            currently_visiting.remove(course)
            visited.add(course)
            
            res.append(course)
        
            return True
        
        # Visit all courses      
        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return res
# @lc code=end

