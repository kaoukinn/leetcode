class Solution:
    def minimumSum(self, num: int) -> int:
        string = str(num) #先把數字轉成字串
        a = sorted(string) #把字串做排序用a變數接起來
        m = a[0] + a[3] #把第一個數字跟第四個數字相加，用變數m代表
        n = a[1] + a[2] #把第二個數字跟第三個數字相加，用變數n代表

        return int(m) + int(n) #最後回傳m跟n相加的結果，要記得轉回整數型態
    



