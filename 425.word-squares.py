class Solution(object):
  
    def backtracking(self, step, word_squares, results):
        
        # Base Case
        if step == self.N:
            results.append(word_squares[:])
            return
        
        # Find the prefix for the next possible word, using the already chosen words in word_squares
        prefix = ''.join([word[step] for word in word_squares])
        
        # Find out all words that start with the given prefix        
        for candidate in self.getWordsWithPrefix(prefix):
            
            # Iterate row by row
            word_squares.append(candidate)
            self.backtracking(step + 1, word_squares, results)
            word_squares.pop()
    
    # Return all words that have the prefix
    def getWordsWithPrefix(self, prefix):
        for word in self.words:
            if word.startswith(prefix):
                yield word


    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """

        self.words = words
        self.N = len(words[0])

        results = []
        word_squares = []
        
        # words = ["area","lead","wall","lady","ball"]
        for word in words:
            
            # Try with every word as the starting word
            word_squares = [word]
            self.backtracking(1, word_squares, results)
            
        return results