#
# @lc app=leetcode id=575 lang=python
#
# [575] Distribute Candies
#

# @lc code=start
class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        # res = 0
        # allowed = len(candyType) // 2

        # candy = Counter(candyType)
        
        # for candie_type in candy.keys():
        #     if allowed > 0 and candy[candie_type] > 0:
        #         res += 1

        #         candy[candie_type] -= 1
        #         allowed -= 1
            
        # return res

        # Short solution
        # The max she can eat is all diff kinds, but if allowed is lesser, then return allowed 
        return min(len(set(candyType)), len(candyType) // 2)
# @lc code=end

