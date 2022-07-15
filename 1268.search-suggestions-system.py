#
# @lc app=leetcode id=1268 lang=python
#
# [1268] Search Suggestions System
#

# @lc code=start
class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.suggestions = []
        
class Trie:
    def __init__(self):
        self.root = Node(None)
        
    def insert(self, word):
        cur = self.root
        
        # First, add a node, then add suggestions, then move down
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node(char)  # -- add node
            
            if len(cur.suggestions) < 3:
                cur.suggestions.append(word)  # ------ add suggestions 
            
            # move further down
            cur = cur.children[char] 
            
        # Since we could only add this last node and not its suggestions above
        # Because it was to be done in  the next iteration
        if len(cur.suggestions) < 3:
            cur.suggestions.append(word)
            
    def find(self, word):
        cur = self.root
        
        res = [] # - collect the suggestions
        
        for _, char in enumerate(word):
            
            # Move to char node and append
            if char in cur.children:
                cur = cur.children[char] # Move cur to char node
                res.append(cur.suggestions) # Append its suggestions
            
            # Deviate: One of the chats in wordSearch doesn't match anything in dictionary
            # Then, add [] for each of the remaining chars
            else:
                break
                
        remaining = len(word) - len(res)
        
        for j in range(remaining):
            res.append([])
                
        return res
    
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        
        # Edge cases: 1 product and 1 match
        if len(products) == 1 and products[0] == searchWord:
            return [[searchWord] for i in range(len(searchWord))]
        
        # For lexicographic order
        products.sort()
        
        root = Trie()
        
        # Build Trie
        for product in products:
            root.insert(product)
            
        return root.find(searchWord)
        
# @lc code=end

