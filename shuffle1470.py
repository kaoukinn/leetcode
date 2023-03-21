# 題目講解:
# 給定一組數值陣列的輸入，我們要把前半部認為是 x 陣列，後半認為是 y 陣列，
# 接著把該數值陣列按照 [x1, y1, x2, y2... xn, yn] 的順序重新排列。

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newlist = []

        for i in range(n):
            newlist.append(nums[i])
            newlist.append(nums[i+n])
        return newlist

程式碼解釋:
# 先建立一個空列表，用迴圈把0-n的數字都抓取出來，然後把nums中的i值加進到空列表，再用nums中的i+n值加進到空列表中
# ex.n代表的是每個循環的數量所以把i+n就會是第二個循環的第一位數字


    


