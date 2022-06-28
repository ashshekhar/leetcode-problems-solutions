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
            
        # Preparation for future
        visited.remove(course)
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
        
        for course in prerequisiteDict.keys():
            # DFS: Visit a course, and its neighbors in DFS fashion
            # If the course can be completed - delete that prerequisite
            
            if not self.dfs(course, prerequisiteDict, visited):
                return False
        
        return True
            
        
# @lc code=end



class Solution():
  def __init__(self):
    pass

  def assignAndPrint(self,t):
    d = dict()
    for pair in t:
      if(pair[0]==pair[1]): # because we dont want to assign self managing role
        continue
      if pair[0] not in d: # assign employee a empty list of employees
        d[pair[0]] = []
      # for managers -
      if pair[1] not in d:
        d[pair[1]] = [pair[0]]
      else:
        d[pair[1]].append(pair[0])

    # now we know how many employees are directly under a particular manager.
    # now lets count the total number of employees under a particular manager.
    c = dict() # store manager:count of employee as key value
    print(d)
    
if __name__=="__main__":
  # t is tuple containing employee and boss pair.
  t = (("A", "C"),("B", "C"),("C", "F"),("D", "E"),("E", "F"),("F", "F"))
  obj = Solution()
  obj.assignAndPrint(t)

