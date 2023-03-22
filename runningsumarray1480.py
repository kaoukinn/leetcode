
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
nums = [12,33,3,5]
s = 0
d = []
for a in nums:
    s += a
    d.append(s)
print(d)

nums = [12, 33, 3, 5]
d = [sum(nums[:i+1]) for i in range(len(nums))]
print(d)