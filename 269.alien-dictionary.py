#
# @lc app=leetcode id=269 lang=python
#
# [269] Alien Dictionary
#

# @lc code=start
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # This is a topological sort problem but the hard part is creating adj list
        
        if not words:
          return ""
        
        # ["aba"] -> Answer should be "ab"
        if len(words) == 1:
          return "".join(c for c in set(words[0]))
        
        adj_list = {c: set() for w in words for c in w}
        
        visited = set()
        currently_visiting = set()
        
        global res
        res = []
        
        # Check each pair of words and detect the first different character
        for i in range(len(words) - 1):
          word1 = words[i]
          word2 = words[i + 1]
          
          minLength = min(len(word1), len(word2))
          
          # Invalid input ordering
          # abde before abd is invalid
          if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
            return  ""
          
          # Valid ordering, now find the first different character
          for j in range(minLength):
            if word1[j] != word2[j]:
              adj_list[word1[j]].add(word2[j])
              break
            
        def dfs(char):
          global res
          
          # Cycle detected on way to traverse the order
          if char in currently_visiting:
            return False
          
          # Already added in topological sort: return True since successfully visited
          if char in visited:
            return True
          
          # Add to current iteration
          currently_visiting.add(char)
          
          for c in adj_list[char]:
            if not dfs(c):
              return False
            
          # On reaching the last char in dfs, prereq would be []
          # So here we remove the last char from currently_visiting
          # And add it to finally visited and outptut.
          currently_visiting.remove(char)
          visited.add(char)
          
          res.append(char)
          
          return True

        # Visit all characters
        for char in adj_list:
          if not dfs(char):
            return ""
        
        # Else reverse the order and return res
        # Because we need to retrieve the smaller to larger ordering
        res.reverse()
        return "".join(res)
# @lc code=end