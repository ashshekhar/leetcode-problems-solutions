#
# @lc app=leetcode id=792 lang=python
#
# [792] Number of Matching Subsequences
#

# @lc code=start
import collections

class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        # Dictionary approach
        # words = ["a","bb","acd","ace"]
        # alpha = {"a": ["a", "acd", "ace"], "b" : ["bb"]}
        
        # Map the values as words waiting for their first char as key
        alpha = collections.defaultdict(list)
        for w in words:
            alpha[w[0]].append(w)
            
        res = 0
        
        for c in s:
            # Extract the words waiting for the char c
            old_bucket = alpha[c]
            
            # Empty the list of c as key since none of them is currently waiting for c
            # Going to already process it
            alpha[c] = []
            
            # For each word in bucket, consider that they received c
            # Now they wait for their next character
            # So we map the rest of the word left (post this c) 
            # to the first char in the left part
            for w in old_bucket:
                next_word = w[1:]
                
                # If there are still some parts of the word waiting for next char
                if next_word:
                    alpha[next_word[0]].append(next_word)
                    
                # If not, then they have been found as a subsequence
                else:
                    res += 1
                
        return res
    
# Simple appraoch but need to visit the whole string s for each word

#     def checkSubsequence(self, s, word):
#         ptr_s = 0
#         ptr_word = 0
        
#         while ptr_word < len(word) and ptr_s < len(s):
#             if word[ptr_word] == s[ptr_s]:
#                 ptr_word += 1
#             ptr_s += 1
        
#         return ptr_word == len(word)
            
#     def numMatchingSubseq(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: int
#         """
#         res = 0
        
#         dp = {}
        
#         for word in words:
#             if word in dp:     
#                 if dp[word] == True:
#                     res += 1
#                 continue

#             if self.checkSubsequence(s, word):
#                 dp[word] = True
#                 res += 1
#             else:
#                 dp[word] = False
        
#         return res
        
# @lc code=end

