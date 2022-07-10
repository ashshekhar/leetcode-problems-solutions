import collections

class Solution:
    def longest_word_chain_len(self, words):
      
        words.sort(key=len)

        # Default val of 0
        dp = collections.defaultdict(int)
        
        for w in words:
            dp[w] = dp[w[:-1]] + 1
        
        # dp -> {'be': 0, 'ben': 1, 'bent': 2, 'de': 0, 'dew': 1, 'den': 1, 'dents': 3, 'dent': 2, 'bet': 1}
        return max(dp.values())

        
s = Solution()
words = ["ben", "bent", "dew", "dents", "dent", "bet", "den"]
assert s.longest_word_chain_len(words) == 3

'''
Time O(NlogN) for sorting,
Space O(NL) where L length of string because of slicing operation in the loop
'''

