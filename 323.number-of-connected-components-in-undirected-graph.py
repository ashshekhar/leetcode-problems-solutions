class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        count = 0
        visited = set()
        adj_list = {i : [] for i in range(n)}
        
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        def dfs(node):
            
            if node in visited:
                return
            
            visited.add(node)
            
            for neighbors in adj_list[node]:
                dfs(neighbors)
            
        
        # Call dfs for each node and only increment count when not in visited
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
        
        return count