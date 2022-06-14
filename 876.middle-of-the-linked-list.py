#
# @lc app=leetcode id=876 lang=python
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
                
        # Slow and fast pointer technique
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Odd cases
        if not fast:
            return slow
        
        # Even cases
        elif not fast.next:
            return slow.next
        
        # Brute Technique
        # nodes = []
        # current = head
        # index = 0
        
        # while current:
        #     nodes.append(index)
        #     index += 1
        #     current = current.next
        
        # mid_index = len(nodes) // 2
        
        # current = head
        # new_index = 0

        # while new_index <= mid_index and current:
        #     if new_index == mid_index:
        #         return current
        #     else:
        #         current = current.next
        #     new_index += 1
        

                 
# @lc code=end

