#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        match = ""
        for i in s:
            match += i
            if(match in wordDict):
                print(f"Inside if: {match}")
                match = ""
                
        print(f"Final match: {match}")
        if(len(match) == 0):
            return True
        return False
           
# @lc code=end

