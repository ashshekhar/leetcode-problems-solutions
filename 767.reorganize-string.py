#
# @lc app=leetcode id=767 lang=python
#
# [767] Reorganize String
#

# @lc code=start
import heapq
from collections import Counter

# The idea is to always append most frequent char, then delete it, 
# add it after next most freq char and so on
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        maxheap = []
        res = []
                
        prev_val, prev_char = 0, ""

        # Heapify and heappop will always act as min heap
        for char in freq:
            heapq.heappush(maxheap, [-freq[char], char])
        
        # "aabb" -> [a:2, b:2] ("") -> [b:2] ("a") (a popped and stored as last val) ->
        # [] ("ab") [a:1] (b popped, a added back, last val updated to b) -> [b:1] ("aba") (a popped again)
        # [] ("abab") (b popped finally and maxheap empty)
        
        while maxheap:
            val, char = heapq.heappop(maxheap)
            res.append(char)
            
            # Push back the char from last iteration
            # It was removed to avoid same char being placed together
            
            # prev_val < 0 means character is still usable as val is negative due to max heap
            if prev_val < 0:
                heapq.heappush(maxheap, [prev_val, prev_char])
            
            # Decrement freq, since val is negative due to max heap
            # Prepare these to be added in next iteration
            val += 1
            prev_val = val
            prev_char = char
            
        if len(res) == len(s):
            return "".join(res)
        
        return ""
# @lc code=end

