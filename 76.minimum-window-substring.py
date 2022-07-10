#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Minimum substring in s that contains all chracters from t
        if t == "" or len(t) > len(s):
            return ""
        
        count_s = {}
        count_t = {}
        
        res = [-1, -1]
        resLength = float("infinity")
        
        # Create the counter for t
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)
        
        # Initialize variables and pointer
        left = 0
        have = 0
        need = len(count_t)
        
        for right, char in enumerate(s):
            count_s[char] = 1 + count_s.get(char, 0)

            # Check if by adding this char we can increase our "have" count
            if char in count_t and count_s[char] == count_t[char]:
                have += 1
            
            # While the condition is met, shrink the window from the left and potentially update result
            # As soon as it it not met, start adding new chars on right
            while have == need:
                
                # Update the result variable, if found a shorter substring
                if (right - left + 1) < resLength:
                    res = [left, right]
                    resLength = right - left + 1
                    
                # Shrink the window
                count_s[s[left]] -= 1
                
                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -= 1

                # Update left pointer
                left += 1
        
        # Return the min substring (not length) if it exists else ""
        return s[res[0] : res[1] + 1] if resLength != float("infinity") else ""
        
# @lc code=end

