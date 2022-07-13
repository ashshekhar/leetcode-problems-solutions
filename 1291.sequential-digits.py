#
# @lc app=leetcode id=1291 lang=python
#
# [1291] Sequential Digits
#

# @lc code=start
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        # Enumerate for all number of possible digits allowed
        main_string = "123456789"
        
        res = []

        for window_len in range(len(str(low)), len(str(high)) + 1):
            i = 0
            j = i + window_len - 1
            
            # Till the end of main_string
            while j < len(main_string):
                possible_seq_digit = main_string[i:j + 1]
                
                if low <= int(possible_seq_digit) <= high:
                    res.append(possible_seq_digit)
                    
                i += 1
                j += 1
    
        return res
        
# @lc code=end

