#
# @lc app=leetcode id=143 lang=python
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        # A better way is to cut the list in half, then reverse the second half 
        # and merge the two node by node
        if not head:
            return
        
        if not head.next:
            return head
        
        # Fast and slow pointer to find the mid of the linked list
        slow = head
        fast = head.next
        mid = None
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        
        # Reverse the second half of the list, but not breaking it off
        prev = None
        next = None
        current = mid

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
            
        # Merge two list node by node
        # Keep in mind, list1 is still connected to the list2, but it works out
        list1 = head
        list2 = prev
        
        while list1 and list2:
            list1_next = list1.next
            list2_next = list2.next
            
            list1.next = list2
            list2.next = list1_next
            
            list1 = list1_next
            list2 = list2_next

        # Place two pointers at end and start and repeat the interchange
        # TLE Code
        # if not head:
        #     return None
        
        # left = head
        
        # current = head
        # count = 1
        
        # prev_right = None
        # right = None
        
        # while current.next:
        #     count += 1
        #     prev_right = current
        #     current = current.next
        #     right = current

        # for _ in range(count // 2  + (count) % 2 - 1):

        #     right.next = left.next
        #     left.next = right
        #     prev_right.next = None
            
        #     # Prepare for next iteration
        #     left = right.next
            
        #     temp = left
            
        #     while temp.next:
        #         prev_right = temp
        #         temp = temp.next
        #         right = temp
# @lc code=end

