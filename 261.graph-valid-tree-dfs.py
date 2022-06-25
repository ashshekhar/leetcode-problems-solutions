class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        
        visited = set()
        
        # Prepare the dictionary
        adj_list = {i : [] for i in range(n)}
        
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        # Need prev_node to detect false positives
        # Since bi directional graph such as: 0 -> 1, 1 -> 0 etc. exists
        # This means that when visiting 1's neighbors 0 will be in visited but is not forming a loop
        def dfs(node, prev_node):
            
            # Cycle detection
            if node in visited:
                return False
                                
            visited.add(node)
            
            for neighbor in adj_list[node]:
                if neighbor == prev_node:
                    continue

                if not dfs(neighbor, node):
                    return False
                
            return True
        
        # Also check if all nodes were visited (Guarantees connection)
        return dfs(0, -1) and len(visited) == n 