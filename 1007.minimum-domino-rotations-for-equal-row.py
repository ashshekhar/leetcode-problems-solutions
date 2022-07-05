#
# @lc app=leetcode id=1007 lang=python
#
# [1007] Minimum Domino Rotations For Equal Row
#

# @lc code=start
class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        # [2,1,2,4,2,2]
        # [5,2,6,2,3,2]
        # Any arbitrary index values will be the common one
        common1 = tops[0]
        common2 = bottoms[0]
        
        # Check for the rest of the indices, either common1 or common2 exists in all
        truth_1 = all( common1 in [tops[i], bottoms[i]] for i in range(1, len(tops)))
        truth_2 = all( common2 in [tops[i], bottoms[i]] for i in range(1, len(tops)))
        final_common = common1 if truth_1 else common2

        # If it doesn't then not possible to make all rows equal
        if not (truth_1 or truth_2):
            return -1

        # Find the array to rotate
        to_rotate = tops if tops.count(final_common) > bottoms.count(final_common) else bottoms

        return len([x for x in to_rotate if x != final_common])
# @lc code=end

