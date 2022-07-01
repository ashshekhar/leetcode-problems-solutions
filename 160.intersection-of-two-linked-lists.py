#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        length_1 = 0
        length_2 = 0
    
        # Find lengths
        currentA = headA
        
        while currentA:
            length_1 += 1
            currentA = currentA.next
        
        currentB = headB
        
        while currentB:
            length_2 += 1
            currentB = currentB.next
        
        # headA and headB point to the same level
        if length_1 > length_2:
            for _ in range(length_1 - length_2):
                headA = headA.next
        
        else:
            for _ in range(length_2 - length_1):
                headB = headB.next
        
        # Iterate and find intersection
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA if headA else None
        
        
# @lc code=end

