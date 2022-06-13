#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next
        
        if list1:
            tail.next = list1

        elif list2:
            tail.next = list2
        
        return dummy.next
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return 
        
        while len(lists) > 1:
            
            # The items in this will be merged in the next iteration
            merged = []
            
            # Merge every 2 LL and add in merged array
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i+1 < len(lists) else None
                
                merged.append(self.mergeTwoLists(l1, l2))

            # The list at each stage now will contain the list of every 2 LL merged
            lists = merged
        
        # Eventually the lists array will contain only one element as the final result
        return lists[0]
        
# @lc code=end

