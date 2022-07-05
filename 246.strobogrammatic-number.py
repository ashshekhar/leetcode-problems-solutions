class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        rotation_map = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        rotated_number = ""
        
        for char in reversed(num):
            
            if char in rotation_map:
                rotated_number += str(rotation_map[char])
                
            else:
                return False
            
        return rotated_number == num
        