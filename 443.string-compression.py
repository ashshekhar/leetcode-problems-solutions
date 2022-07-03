#
# @lc app=leetcode id=443 lang=python
#
# [443] String Compression
#

# @lc code=start
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # Two pointer solution
        
        # One pointer to iterate the chars array
        counter = 1
        
        # The other pointer to overwrite chars array
        overwrite = 0
        
        if len(chars) == 1:
          return 1
        
        for i in range(1, len(chars)):
          if chars[i] == chars[i - 1]:
            counter += 1
            
          else:
            chars[overwrite] = chars[i - 1]
            overwrite += 1
            
            if counter > 1:
              for x in str(counter):
                chars[overwrite] = str(x)
                overwrite += 1
            
            # Reset for next new char already at chars[i]
            counter = 1
        
        chars[overwrite] = chars[i]
        overwrite += 1
            
        if counter > 1:
          for x in str(counter):
            chars[overwrite] = str(x)
            overwrite += 1
        
        return overwrite
        
# @lc code=end

