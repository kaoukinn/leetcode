
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ans = []
        a = 0
        for num in nums:
            a += num
            ans.append(a)
        print(ans)