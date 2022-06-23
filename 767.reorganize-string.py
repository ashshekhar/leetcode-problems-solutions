#
# @lc app=leetcode id=767 lang=python
#
# [767] Reorganize String
#

# @lc code=start
import heapq
from collections import Counter

# The idea is to always append most frequent char and delete it, add it after next most freq char
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

        while maxheap:
            val, char = heapq.heappop(maxheap)
            res.append(char)
            
            # Push back the char from last iteration
            # It was removed to avoid same char being placed together
            if prev_val < 0:
                heapq.heappush(maxheap, [prev_val, prev_char]) # put previous char to heap again after popping new char
            
            # Decrement freq
            val += 1

            prev_val = val
            prev_char = char
            
        if len(res) == len(s):
            return "".join(res)
        
        return ""
        
# @lc code=end

