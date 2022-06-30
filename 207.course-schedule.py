#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start
class Solution(object):    
    def dfs(self, course, prerequisiteDict, visited):
        
        # Cycle Detection
        if course in visited:
            return False
        
        # Base case
        if prerequisiteDict[course] == []:
            return True
        
        visited.add(course)

        for prereqs in prerequisiteDict[course]:
            if not self.dfs(prereqs, prerequisiteDict, visited):
                return False
            
        # Cleaning: We are no longer visiting course
        visited.remove(course)
        
        # And since the for loop did not return False ever, then course can be completed
        prerequisiteDict[course] = []
        
        return True
                   
            
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Concept of topological sort
        # If there is a cycle then you can't finish all the courses, else see if you can
        
        prerequisiteDict = {i: [] for i in range(numCourses)}
        
        for courses in prerequisites:
            prerequisiteDict[courses[0]].append(courses[1])

        visited = set()
        
        # Call DFS on all courses
        for course in range(numCourses):
            # DFS: Visit a course, and its neighbors in DFS fashion
            # If the course can be completed - delete that prerequisite
            
            if not self.dfs(course, prerequisiteDict, visited):
                return False
        
        return True
            
        
# @lc code=end