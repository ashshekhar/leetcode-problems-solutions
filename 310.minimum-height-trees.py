#
# @lc app=leetcode id=310 lang=python
#
# [310] Minimum Height Trees
#

# @lc code=start
class Solution(object):
          
    # The better and expected approach is to trim out the leaf nodes until
    # there are only 2 or 1 node(s) left which will be our answer
    
    # This is because centroid is the closest to the circumference of the circle
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        if not edges:
            return [n - 1]
        
        # Trim the leaves until only two or one are left
        adj_list = {i: [] for i in range(n)}
        leaves = []
        
        # Adjacency list
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        # Only one attachment to its parent, so leaf node
        for node in adj_list.keys():
            if len(adj_list[node]) == 1:
                leaves.append(node)
        
        nodes_left = n
        
        while nodes_left > 2:
            
            nodes_left -= len(leaves)
            new_leaves = []
            
            while leaves:
                leaf = leaves.pop()
                only_parent = adj_list[leaf].pop()
                
                adj_list[only_parent].remove(leaf)
                
                if len(adj_list[only_parent]) == 1:
                    new_leaves.append(only_parent)
            
            leaves = new_leaves
    
        return leaves
        
    # Can't simply return the max of left side and right side since not a tree
    # So, will need to run a DFS on each neighbor
    # TLE Solution
        
    # def findMinHeightTrees(self, n, edges):
    #     """
    #     :type n: int
    #     :type edges: List[List[int]]
    #     :rtype: List[int]
    #     """
    #     # You can find the height of a tree n times
    #     adj_list = {i: [] for i in range(n)}
        
    #     res = []
    #     visited = set()
        
    #     global max_height
    #     max_height = 0
        
    #     for edge in edges:
    #         adj_list[edge[0]].append(edge[1])
    #         adj_list[edge[1]].append(edge[0])
            
        
    #     # Find max height from node
    #     def dfs(index, node):

    #         global max_height 
        
    #         if node in visited:
    #             return

    #         visited.add(node)

    #         max_height = max(max_height, index)

    #         for neighbors in adj_list[node]:
    #             if neighbors not in visited:
    #                 dfs(index + 1, neighbors)

    #         return max_height
    
    #     # Find the heights for all nodes as root
    #     for i in range(n):
            
    #         max_height = 0
    #         visited = set()
    #         res.append(dfs(0, i))
        
    #     minimum_val = min(res)
    #     return [ind for ind, val in enumerate(res) if val == minimum_val]
# @lc code=end