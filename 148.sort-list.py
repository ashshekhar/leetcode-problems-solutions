#
# @lc app=leetcode id=148 lang=python
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def findMid(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Base cases
        if not head or not head.next:
            return head
        
        # Split into halves
        left = head
        
        right = self.findMid(head)
        temp = right.next
        right.next = None
        
        right = temp
        
        # Sort both halves recursively
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.mergeSortedLists(left, right)
    
    def mergeSortedLists(self, l1, l2):
        tail = dummy = ListNode()
        
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
            
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
            
        return dummy.next
        
# @lc code=end

