nums = [10,4,8,3]

n = len(nums)
leftnums, rightnums, ansnums = [0]*n,[0]*n,[0]*n

for i in range(1, n):
    leftnums[i] = leftnums[i-1] + nums[i-1]
for a in range(n-2, -1, -1):
    rightnums[a] = rightnums[a+1] + nums[a+1]

for i in range(n):
    ansnums[i] = abs(leftnums[i] - rightnums[i])

print(ansnums)
