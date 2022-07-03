class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
                    
        num1 = A    
        num2 = B
        
        # Base cases
        if num1 == 0:
            return num2
        if num2 == 0:
            return num1

        if num2 % num1 == 0:
            return num1

        res = self.gcd(num2 % num1, num1)
        
        return res