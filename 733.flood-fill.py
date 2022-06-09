#
# @lc app=leetcode id=733 lang=python
#
# [733] Flood Fill
#

# @lc code=start
class Solution(object):
    def dfs(self, image, original_val, sr, sc, rows, columns, newColor):
        if sr >= rows or sr < 0 or sc >= columns or sc < 0 or image[sr][sc] != original_val or image[sr][sc] == newColor:
            return
        
        image[sr][sc] = newColor
        
        self.dfs(image, original_val, sr, sc-1, rows, columns, newColor)
        self.dfs(image, original_val, sr, sc+1, rows, columns, newColor)
        self.dfs(image, original_val, sr-1, sc, rows, columns, newColor)
        self.dfs(image, original_val, sr+1, sc, rows, columns, newColor)
        
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        columns = len(image[0])
        original_val = image[sr][sc]
        
        self.dfs(image, original_val, sr, sc, rows, columns, newColor)
        
        return image        

# @lc code=end

