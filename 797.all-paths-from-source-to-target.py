#
# @lc app=leetcode id=797 lang=python
#
# [797] All Paths From Source to Target
#

# @lc code=start
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
                
        source = 0
        target = len(graph) - 1
        
        global res
        res = []
        
        def backtrack(node, path):

            global res
            
            if node == target:
                res.append(path[::])
                return
            
            for neighbors in graph[node]:
                path.append(neighbors)
                backtrack(neighbors, path)
                path.pop()
            
        
        path = []
        path.append(source)
        
        backtrack(source, path)
        
        return res
# @lc code=end

