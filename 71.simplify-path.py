#
# @lc app=leetcode id=71 lang=python
#
# [71] Simplify Path
#

# @lc code=start
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # .. means pop the last directory 
        # ["., /"] can be ignored
        # Final path can't end with "/"
        # Should start with a single "/"
        
        # /home//mkd/../path becomes = ["", "home", "", "mkd", "..", "path"]
        # So multiple /// together are reduced to one null string
        path = path.split("/")
        
        stack = []
        
        
        for items in path:
            if not items or items == ".":
                continue
                
            elif items == "..":
                if stack:
                    stack.pop()
                    
            else:
                stack.append(items)

        return "/" + "/".join(stack)
        
# @lc code=end

