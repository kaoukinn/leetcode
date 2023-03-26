class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or not cloned: # 這段是用來判斷輸入的origin跟cloned是否為空，
            return None  # 因為如果其中一個為空在遞規函數就會出現錯誤，所以為了避免錯誤要在這邊設定檢查條件
            
        if original == target:  # 如果original等於target就回傳cloned
            return cloned

        left_copy = self.getTargetCopy(original.left, cloned.left, target) #再來判斷左節點跟右節點是否等於target
        right_copy = self.getTargetCopy(original.right, cloned.right, target) #如果等於先用變數接起來

        return left_copy or right_copy  #最後再回傳該變數