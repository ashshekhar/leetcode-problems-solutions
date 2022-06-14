#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Run the algorithm on paper to understand
        if not head:
            return None
        
        current = head
        history = None
        
        while current and current.next:
            orig_prev = current
            orig_next = current.next
            
            if current.next.next:
                next_to_process = current.next.next
            else:
                next_to_process = None
            
            orig_next.next = orig_prev
            
            if history:
                history.next = orig_next
                
            orig_prev.next = next_to_process
            
            if current == head:
                head = orig_next
            
            history = orig_prev
            orig_prev = None
            orig_next = None
            current = next_to_process
            
        return head
        
# @lc code=end

