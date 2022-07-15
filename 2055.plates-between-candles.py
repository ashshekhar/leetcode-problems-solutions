#
# @lc app=leetcode id=2055 lang=python
#
# [2055] Plates Between Candles
#

# @lc code=start
import bisect

class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # List of candle indices
        A = [index for index, char in enumerate(s) if char == '|']

        res = []
        
        for a,b in queries:
            
            # Left-most index where you can insert a
            i = bisect.bisect_left(A, a)
            
            # Right-most index where you can insert b - 1
            j = bisect.bisect_right(A, b) - 1
            
            # A[j] - A[i] - 1 is the space between two candles
            # j - i - 1 is the number of candles in between the above two candles
            # (A[j] - A[i] - 1) - (j - i - 1) is the number of plates between two candles

            res.append((A[j] - A[i]) - (j - i) if i < j else 0)
            
        return res
# @lc code=end

