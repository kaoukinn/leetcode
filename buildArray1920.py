class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans_list = []

        for i in nums:
            # if nums[i] not in ans_list:
            ans_list.append(nums[i])
            
        return ans_list