class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n*2
        
# 算出最小公倍數，如果n除2可以整除就回傳n，如果不行就回傳n*2