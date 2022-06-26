#
# @lc app=leetcode id=877 lang=python
#
# [877] Stone Game
#

# @lc code=start
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # Both Alice and Bob can see the array
        
        # Easy approach
        # If sum is always odd: Alice just needs to choose max of all even numbers or all odd numbers
        # Therefore, she will always win or
    
        # Harder approach
        # If sum is not always odd: Then we need to use DP and caching because Alice will have 2 choices at each stage
        
        # This dp[(i, j)] will store the max sum Alice can get within the subarray from i to j
        dp = {}
        
        def dfs(left, right):
            
            if left > right:
                return 0
            
            if (left, right) in dp:
                return dp[(left, right)]

            # If not cached, then make Alice take the optimal decision and store it in dp
            alice_turn = True if (right - left) % 2 else False
            
            if alice_turn:
                left_pick = piles[left]
                right_pick = piles[right]
            else:
                left_pick = 0
                right_pick = 0
            
            # Recursive DP Call and Caching
            dp[(left, right)] = max(left_pick + dfs(left + 1, right), right_pick + dfs(left, right - 1))            
            
            return dp[(left, right)]
        
        # Return True if Alice got the sum greater than half of array sum
        # Since Bob's sum = Array sum - Alice's
        alice_max_sum = dfs(0, len(piles) - 1)
        return alice_max_sum > (sum(piles) - alice_max_sum)
        
# @lc code=end

