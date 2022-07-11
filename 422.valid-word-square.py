class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in range(len(words)):
            rowWord = words[i]
            colWord = []
            
            for j in range(len(words)):
                
                # If the current index i is strictly less than the word at jth index
                if i < len(words[j]):
                    colWord.append(words[j][i])
            
            # Check if the two words were equal
            if rowWord != ''.join(colWord):
                return False
            
        return True