class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pairs = [['0', '0'], ['1', '1'], ['6', '9'], ['8', '8'], ['9', '6']]
        
        
        def recursion(cur_n, n, pairs):

            # Base cases
            if cur_n == 0:
                return [""]

            if cur_n == 1:
                return ["0", "1", "8"]
            
            # Recurse with n - 2
            prev_nums = recursion(cur_n - 2, n, pairs)
            cur_nums = []

            for prev_num in prev_nums:
                for pair in pairs:
                    
                    # Ignore leading 0's numbers
                    if pair[0] == '0' and cur_n == n:
                        continue

                    cur_nums.append(pair[0] + prev_num + pair[1])

            return cur_nums
        
        return recursion(n, n, pairs)