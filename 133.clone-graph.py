#
# @lc app=leetcode id=133 lang=python
#
# [133] Clone Graph
#

# @lc code=start

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        # Mapping old and new clone nodes
        dictionary = dict()
        
        # Recursively creating clones in DFS fashion
        def dfs(node):
            # If clone already exists
            if node in dictionary:
                return dictionary[node]
            
            # Make new clone and add to hashmap
            copied_node = Node(node.val, [])
            dictionary[node] = copied_node
            
            # Next, also need to clone neighbors
            for neighbor in node.neighbors:
                copied_node.neighbors.append(dfs(neighbor))
                    
            return copied_node
        
        # Since it is a completely connected graph, just calling it once
        # creates the whole graph clone
        return dfs(node)
# @lc code=end

