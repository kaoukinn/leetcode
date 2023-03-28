class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == None: #先確認輸入的列表有沒有東西，如果沒有回傳空值
            return None

        i, j = 0, 1 # 先用兩個變數來代表兩個指針

        while j < len(nums):  #如果j小於列表長度才進行下面的程式碼
            if nums[i] != nums[j]: #在判斷nums[i] 是否不等於 nums[j]
                i += 1 #不等於的話就把i+1
                nums[i] = nums[j] #把j指向的值賦予給i指向的值
            j += 1 #再把j+1讓他往下繼續跑
        return i + 1  #最後回傳i+1==而不是i因為i是從0開始
