#
# @lc app=leetcode id=648 lang=python
#
# [648] Replace Words
#

# @lc code=start
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.prefix = ""
        
class Trie(object):
    def __init__(self):
        self.data = TrieNode()
        
    def insert(self, word):
        current = self.data
        
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            
            current = current.children[char]
            
        current.prefix = word
        current.endOfWord = True
        
    # Return a prefix if it exists, else return the word itself
    def returnPrefix(self, word):
        current = self.data
        
        for char in word:
            # print(word,char)
            if char not in current.children:
                return word
            
            # Else check next
            current = current.children[char]
            
            # Found the prefix
            if current.endOfWord:
                return current.prefix
            
        return word
        
        
class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        sentence = sentence.split(" ")
        dictionary = set(dictionary)
        
        # Trie Solution
        root_trie = Trie()

        # Insert the dictionary in Trie structure
        for roots in dictionary:
            root_trie.insert(roots)
        
        # Replace using dictionary
        for i in range(len(sentence)):
            
            pre = root_trie.returnPrefix(sentence[i])

            if sentence[i] != pre:
                sentence[i] = pre
        
        return  " ".join(sentence)
                

        # Simple solution
        # for i in range(len(sentence)):
        #     for j in range(len(sentence[i])):
        #         if sentence[i][:j] in dictionary:
        #             sentence[i] = sentence[i][:j]
                    
        # return " ".join(sentence)
        
# @lc code=end

