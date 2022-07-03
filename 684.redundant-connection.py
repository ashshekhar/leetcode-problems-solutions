#
# @lc app=leetcode id=684 lang=python
#
# [684] Redundant Connection
#

# @lc code=start
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Keeping track of visited is not going to work
        # Use Union-Find Algorithm to detect cycles
        n = len(edges)
        
        # Initially, every node is its own parent
        parents = [i for i in range(n + 1)]
        
        # Initially, every node has rank 1
        rank = [1 for i in range(n + 1)]
        
        # Find the root (top-most) parent of this node
        def find(node):
            parent = parents[node]
            
            # But you might need to go deeper, 
            # and stop when the parent is its own parent like the top root
            while parent != parents[parent]:
                parent = parents[parent]
                
            return parent
        
        # Return False if cycle, else union the nodes and return True
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            
            # Same parent: Cycle detected
            if parent1 == parent2:
                return False
            
            # parent1 will be the parent of both parents
            if rank[parent1] > rank[parent2]:
                rank[parent1] += rank[parent2]
                parents[parent2] = parent1
            else:
                rank[parent2] += rank[parent1]
                parents[parent1] = parent2
            
            return True
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return [edge[0], edge[1]]
# @lc code=end

