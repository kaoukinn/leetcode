nums = [11, 15, 2, 7]  
target = 9
for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j] == target-nums[i]:
                    print(i,j)