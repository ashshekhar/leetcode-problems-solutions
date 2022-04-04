#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_1 = []
        num_2 = []
        
        while l1:
            num_1.append(l1.val)
            l1 = l1.next
            
        while l2:
            num_2.append(l2.val)
            l2 = l2.next
        
        dec_1 = 0    
        for i in range(len(num_1)):
            dec_1 += num_1[i] * (10**i)
            
        dec_2 = 0    
        for i in range(len(num_2)):
            dec_2 += num_2[i] * (10**i)
            
        # Now we have the number - Convert it to reverse linked list
        l3 = ListNode()
        dummy = l3
        
        for num in str(dec_1+dec_2)[::-1]:
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        return l3.next
            
# @lc code=end