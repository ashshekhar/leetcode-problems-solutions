# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
       
from collections import deque

class NestedInteger(object):
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        # Code using the BFS approach
        # Catch is to detect a list, send it back to the end of the queue
        # Also, increase depth after each level
        
        depth = 1
        queue = deque(nestedList)
        res = 0
        
        while queue:
            
            for  _ in range(len(queue)):
                item = queue.popleft()
                
                # If the item is an integer, then extract the integers and add to result
                if item.isInteger():
                    res += depth * item.getInteger()
                
                # If the item is a list, then append to the end of the list
                # extend is used to "extend" the queue with the numbers inside the item
                # extend takes in an iterator and appends the items in that to end
                else:
                    queue.extend(item.getList())
            
            # Next depth level
            depth += 1
        
        return res