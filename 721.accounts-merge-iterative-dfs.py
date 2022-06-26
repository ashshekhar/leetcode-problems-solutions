#
# @lc app=leetcode id=721 lang=python
#
# [721] Accounts Merge
#

# @lc code=start
import collections

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        adj_list_graph = collections.defaultdict(set)
        email_to_name = collections.defaultdict(set)

        final = []
        stack = []
        
        visited = set()
        
        # Mapping the first email to all others and reverse
        # Also creating name dictionary
        for account in accounts:
            name = account[0]
            email_to_name[account[1]] = name

            for i in range(1, len(account)):
                adj_list_graph[account[1]].add(account[i])
                adj_list_graph[account[i]].add(account[1])
                email_to_name[account[i]] = name

        # Running iterative DFS
        for email in adj_list_graph:
            if email not in visited:
                
                stack.append(email)
                visited.add(email)

                res = []

                while stack:
                    node = stack.pop()      
                    res.append(node)

                    for neighbors in adj_list_graph[node]:
                        if neighbors not in visited:
                            stack.append(neighbors)
                            visited.add(neighbors)

                final.append([email_to_name[email]] + sorted(res))

        return final
        
# @lc code=end