#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        # Final result
        res = []
        
        # Each path with their characters separated
        current = []
        
        # Phone number - character combination
        combination = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                     "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        
        # Draw the decision tree to understand better
        # Different than previous backtrackign questions - Use of for loop inside
        def backtrack(index):
            
            if index >= len(digits):
                res.append("".join(current))
                return
            
            for letter in combination[digits[index]]:
                # Choose one of the allowed chars at index i
                current.append(letter)
                
                backtrack(index + 1)
                
                current.pop()
                
        backtrack(0)
        return res
# @lc code=end

