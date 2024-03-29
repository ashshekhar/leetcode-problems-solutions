#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Change val to None approach
        node = head
        
        while node is not None:
            if node.val is not None:
                node.val = None
            else:
                return True
            
            node = node.next

        # Fast and slow pointer approach
        # If ever equal, guarantees a cycle
        # if not head:
        #     return False
        
        # slow, fast = head, head
        
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
            
        #     if slow == fast:
        #         return True
            
        # return False
# @lc code=end

