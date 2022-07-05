#
# @lc app=leetcode id=904 lang=python
#
# [904] Fruit Into Baskets
#

# @lc code=start
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        if len(fruits) <= 2:
            return len(fruits)
        
        fruit_map = {}
        res = 0
        i = 0
    
        # Prepare initial dictionary such that at least 2 types are there
        while i < len(fruits) and len(fruit_map) < 2:
            fruit_map[fruits[i]] = 1 + fruit_map.get(fruits[i], 0)
            i += 1
        
        # To traverse the rest of the array
        left = 0
        right = i
        res = max(res, sum(fruit_map.values()))
        
        while left <= right and right < len(fruits):
            
            # If fruit of this type already exists, just increase the number
            if fruits[right] in fruit_map:
                fruit_map[fruits[right]] += 1
            
            # If it doesn't then first add the new fruit type and 
            # then keep deleting the old ones till the length is back to 2
            else:
                fruit_map[fruits[right]] = 1 + fruit_map.get(fruits[right], 0)
                
                while len(fruit_map) > 2:
                    
                    fruit_map[fruits[left]] -= 1
                    
                    if fruit_map[fruits[left]] == 0:
                        del fruit_map[fruits[left]]
                        
                    left += 1
                    
            res = max(res, sum(fruit_map.values()))
            right += 1
        
        return res          

# @lc code=end

