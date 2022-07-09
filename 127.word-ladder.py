#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder
#

# @lc code=start
import collections
from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        count = 1
        
        if endWord not in wordList:
            return 0
        
        # Tricky graph problem - Trick is in creating and using adjacency list
        patterns = collections.defaultdict(list)
        
        wordList.append(beginWord)
        
        # Creating the adjacency list
        for word in wordList:
            for j in range(len(word)):
                temp = word[:j] + "*" + word[j+1:]
                patterns[temp].append(word)
        
        # Run BFS from start word to end word
        queue = deque([beginWord])
        visited = set([beginWord])
        
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                
                if word == endWord:
                    return count
                
                # Else explore the neighbors of this word
                # Reconstruct all the possible patterns of this word and use the adj list
                for j in range(len(word)):
                    temp = word[:j] + "*" + word[j+1:]
                    
                    for words in patterns[temp]:
                        if words not in visited:
                            visited.add(words)
                            queue.append(words)
                    
            count += 1
        
        # Unable to find the endWord
        return 0
# @lc code=end


