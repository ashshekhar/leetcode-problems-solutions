#
# @lc app=leetcode id=895 lang=python
#
# [895] Maximum Frequency Stack
#

# @lc code=start
class FreqStack(object):

    def __init__(self):
        # Counter for numbers appearing in push
        self.counter = dict()
        
        # Dictionary that maps number of occurences to a stack
        self.count_list = dict()
        
        # To easily pop
        self.max_count = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val not in self.counter:
            self.counter[val] = 1
        else:
            self.counter[val] += 1
        
        if self.counter[val] > self.max_count:
            self.max_count = self.counter[val]
            self.count_list[self.counter[val]] = []
        self.count_list[self.counter[val]].append(val)
        
        # This creates the following
        # Input: 5, 7, 5, 4, 7, 5
        # counter = {5:3, 7:2, 4:1}
        # counter_list = {1: [5, 7, 4], 2: [5, 7], 3: [5]}
        # So just keep poping the elements in the stack at max_count key
            
    def pop(self):
        """
        :rtype: int
        """
        res = self.count_list[self.max_count].pop()
        
        self.counter[res] -= 1
        
        if not self.count_list[self.max_count]:
            self.max_count -= 1
        
        return res
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

