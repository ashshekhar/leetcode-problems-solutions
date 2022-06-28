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
        dummy = ListNode(0, head)
        
        # Find left and previous to left nodes
        left_node = head
        node_before_left = dummy
        temp = left
        
        while temp > 1:
            node_before_left = left_node
            left_node = left_node.next
            temp -= 1

        # Find the right node
        right_node = head
        temp = right
        
        while temp > 1:
            right_node = right_node.next
            temp -= 1
            
        # Reversing the portion
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
        
        return dummy.next
    
# @lc code=end