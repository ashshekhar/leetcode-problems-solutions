class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        made_one_edit_already = False
        
        # Can never be one edit distance
        if (s == t) or (abs(len(s) - len(t)) > 1):
            return False
        
        # Let's convert s to t
        top = 0
        bottom = 0
        
        while top < len(s) and bottom < len(t):
            if s[top] == t[bottom]:
                top += 1
                bottom += 1
                
            else:
                if made_one_edit_already:
                    return False
                
                made_one_edit_already = True
                
                # Delete current char in s and move top pointer to next
                if len(s) > len(t):
                    top += 1
                    
                # Insert char before current char in s and move bottom pointer to next
                elif len(s) < len(t):
                    bottom += 1
                    
                # Replace if lengths are equal
                else:
                    top += 1
                    bottom += 1
        
        # Successfully made to the end of both strings with one edit
        return True