#
# @lc app=leetcode id=2130 lang=python
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        if not head:
            return
        
        # Stores the max of all twin sums
        res = 0
        half = []
        
        slow = head
        fast = head.next
        
        # slow will point at midpoint
        while fast.next:
            half.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        half.append(slow.val)
        next_half = slow.next  
        index = len(half) - 1

        # Traverse second half and add reverse of first half values
        while next_half:
            res = max(res, next_half.val + half[index])
            index -= 1
            next_half = next_half.next
        
        return res
   
# @lc code=end

