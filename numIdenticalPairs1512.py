class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0  #計數器
        dight = {}  #空字典
        for num in nums:  #把每個數字都從list中抓出來
            count += dight.setdefault(num, 0) 
            dight[num] += 1
        return count
