#
# @lc app=leetcode id=61 lang=python
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        if not head.next or k == 0:
            return head
        current = head
        count = 0
        
        while current:
            count += 1
            current = current.next
        
        rotations = k % count
        
        if rotations == 0:
            return head
          
        # Method for actually rotating 'rotations' times
        # left = head
        # last = head
        
        # for _ in range(rotations):
        #     while last.next.next is not None:
        #         last = last.next
            
        #     # Rotating
        #     last.next.next = left
        #     left = last.next
        #     last.next = None
            
        #     # Reset for next loop
        #     last = left
            
        # return left
        
        # Method for leveraging the 'rotations' value
        # Break the linked list where it should after k rotations
        left_count = count - rotations

        i = 1
        current = head
        
        while i != left_count:
            current = current.next
            i += 1
        
        # Break list at appropriate point 
        next_half = current.next
        current.next = None
        new_start = next_half
        
        while next_half.next != None:
            next_half = next_half.next

        next_half.next = head
        
        return new_start
            
# @lc code=end

