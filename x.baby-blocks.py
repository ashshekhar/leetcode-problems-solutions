import collections

class Solution:
    def BabyPairs(self, string, pairs):
      
        if string == None or pairs == None:
            return None
          
        visited = set()
        
        def dfs(word, index):

            # If we have reached the end
            if index == len(word):
                return True
            
            # If char at index is not in pairs - doesn't come from any input tuple
            if word[index] not in store_pairs.keys():
                return False
            
            valid = False
            
            # List of all tuples containing this char
            index_pair = store_pairs[word[index]]
            
            for pair in index_pair:

                # If there is a usable tuple not used, use it and call DFS
                if pair not in visited:
                    visited.add(pair)
                    
                    # Any False value will make valid False and hence the whole answer
                    valid = valid or dfs(word, index + 1)
                    
                    # Backtracking
                    visited.remove(pair)
 
            return valid
              
        store_pairs = collections.defaultdict(set)
        
        # For each char in each pair, match it to the tuple it is from
        # {'b': {('a', 'b'), ('b', 'a')}, 'a': {('a', 'b'), ('b', 'a')}, 
        # 'l': {('l', 'e')}, 'e': {('l', 'e')}, 'c': {('c', 'd')}, 
        # 'd': {('c', 'd')}})
        
        for pair in pairs:
            store_pairs[pair[0]].add(tuple(pair))
            store_pairs[pair[1]].add(tuple(pair))

        # Start at index 0
        return dfs(string, 0)
        
    
if __name__ == '__main__':
  
  sol = Solution()
  print(sol.BabyPairs('babyf', [['b', 'a'], ['a','b'], ['b', 'c'], ['e', 'f'], ['x', 'y']]))
  print(sol.BabyPairs('bablexx', [['b', 'a'], ['a','b'], ['l', 'e'], ['c', 'd']]))