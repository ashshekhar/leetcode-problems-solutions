class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        key_dict = {}
        res = 0
        
        for index, value in enumerate(keyboard):
            key_dict[value] = index 
        
        res = key_dict[word[0]]

        for i in range(1, len(word)):
            res += abs(key_dict[word[i]] - key_dict[word[i - 1]])
    
        return res