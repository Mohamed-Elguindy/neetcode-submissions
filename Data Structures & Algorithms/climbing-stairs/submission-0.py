class Solution:
    def climbStairs(self, n: int) -> int:
        one_step=1
        two_step=1
        if n == 1 or n == 0:
            return 1
        total=0    
        for i in range (0,n-1):
            total =one_step+two_step
            two_step=one_step
            one_step=total
        return total

        