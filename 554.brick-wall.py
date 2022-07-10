#
# @lc app=leetcode id=554 lang=python
#
# [554] Brick Wall
#

# @lc code=start
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # Records gap location (in terms of sum of brick widths) : Count of gaps at the same location
        gap_count = {0 : 0}
   
        for rows in wall:
            gaps = 0     
            
            # For all bricks except last
            for bricks in rows[:-1]:
                gaps += bricks
                gap_count[gaps] = 1 + gap_count.get(gaps, 0)
        
        # Min cuts implies, total rows (= len(wall)) - position of max gap
        return len(wall) - max(gap_count.values())
# @lc code=end

