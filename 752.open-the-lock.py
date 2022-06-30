#
# @lc app=leetcode id=752 lang=python
#
# [752] Open the Lock
#

# @lc code=start
from collections import deque
class Solution(object):
    
    # For each string, there are 8 possible next strings, since +1 and -1 for each char
    def findChildren(self, combination):
        res = []
        
        for i in range(len(combination)):
            
            # Permutation +1
            nxt = str((int(combination[i]) + 1) % 10)
            res.append(combination[:i] + nxt + combination[i+1:])
        
        
            # Permutation -1
            nxt = str(((int(combination[i]) - 1) + 10) % 10)
            res.append(combination[:i] + nxt + combination[i+1:])
        
        return res
    
    # Basically we are going to be brute forcing all possibilities while avoiding duplicates
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if "0000" in deadends:
            return -1
        
        # Never visit these again
        visited = set(deadends)
        
        queue = deque()
        queue.append((0, "0000"))
        
        while queue:
            turns, combination = queue.popleft()
            
            # Base case
            if combination == target:
                return turns
            
            # Find next
            children = self.findChildren(combination)
            
            # Never visit the deadends or same children again
            for child in children:
                if child not in visited:
                    visited.add(child)
                    queue.append((turns + 1, child))
        
        return -1 
        
# @lc code=end

