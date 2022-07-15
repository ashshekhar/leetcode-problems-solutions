class Solution(object):
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        ones = data.count(1)
        flag = False
        
        if ones == 1:
            return 0
        
        zeroes_win_end_index = len(data) - ones - 1
 
        left = 0
        right = len(data) - 1
        res = 0
        
        while left <= zeroes_win_end_index and right > zeroes_win_end_index:
            flag = False
            
            if data[left] == 1:
                while data[right] != 0 and right > zeroes_win_end_index:
                    flag = True
                    right -= 1
                
                if flag:
                    res = res + 1
                    
            elif data[right] == 0:
                while data[left] != 1 and left <= zeroes_win_end_index:
                    flag = True
                    left += 1
                
                if flag:
                    res = res + 1
            
            left += 1
            right -= 1
                
        return res