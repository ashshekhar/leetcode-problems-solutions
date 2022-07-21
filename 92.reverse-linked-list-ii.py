#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
#

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head:
            return 
        
        # dummy node will always point to the current / new head
        dummy = ListNode(0, next = head)
        
        # Find left and previous to left nodes
        left_node = head
        node_before_left = dummy
        temp = left
        
        while temp > 1:
            node_before_left = left_node
            left_node = left_node.next
            temp -= 1
            
        # Reversing the portion required number of times
        prev = None
        nxt = None
        
        for _ in range(right - left + 1):
            nxt = left_node.next
            left_node.next = prev
            prev = left_node
            left_node = nxt
            
        # Final connections
        node_before_left.next.next = nxt
        node_before_left.next = prev
        
        # Can't simply return head, because for [1, 2] -> [2, 1] head is modified
        # Either dummy keeps pointing at original head, like example 1
        # Or the head is modified, so node_before_left and dummy are the same
        # and last line (node_before_left.next = prev = dummy.next which is the new head
        return dummy.next
    
# @lc code=end