#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        length = 0
        current = head
        
        while current:
            length += 1
            current = current.next
        
        index_to_remove = length - n
        
        index = 0 
        current = head
        prev = None
        
        while index != index_to_remove and current:
            prev = current
            current = current.next
            index += 1
        
        if index_to_remove == 0 and length == 1:
            head = None
            
        elif index_to_remove == 0 and length > 1:
            head = head.next
        
        else:
            prev.next = current.next
            
        return head
        
# @lc code=end

