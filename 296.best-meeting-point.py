class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = []
        cols = []
        res = 0
        
        # Prepare the rows and cols to find median
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
                    
        rows.sort()
        cols.sort()
        
        # Median is the ideal meeting point
        # Median is simply the middle most value
        ideal_meeting_point = (rows[len(rows)//2], cols[len(cols)//2])

        # Calculate Manhattan Distance with the median
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += abs(i - ideal_meeting_point[0]) + abs(j - ideal_meeting_point[1])
                    
        return res

