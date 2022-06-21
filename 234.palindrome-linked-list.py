#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return None
        
        if not head.next:
            return True
        
        slow = head
        fast = head.next
        
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        palindrome_start = slow.next
        
        # Reverse the second half of the linked list 
        current = palindrome_start
        prev = None
        next = None
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        # Check palindrome now
        start = head
        palindrome_start = prev

        while palindrome_start:
            if start.val != palindrome_start.val:
                return False
            
            start = start.next
            palindrome_start = palindrome_start.next
            
        return True
        
        
        
# @lc code=end

