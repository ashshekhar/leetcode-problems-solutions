#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # Simply create the nodes and add to hashmap for future reference
        # Add one mapping which is needed
        orig_to_copy = {None: None}
        
        # Can't map to the next because the copy of next pointer is not created yet
        current = head
        while current:
            copy = Node(current.val)
            orig_to_copy[current] = copy
            current = current.next

        # Now add the pointers
        current = head
        while current:
            
            copy = orig_to_copy[current]
            
            # Need a None mapping
            copy.next = orig_to_copy[current.next]
            copy.random = orig_to_copy[current.random]
            
            current = current.next
            
        return orig_to_copy[head]
            
        
# @lc code=end

