class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        addition = ["X++","++X"]
        subtraction = ["--X","X--"]
        for i in operations:
            if i in addition:
                x += 1
            else:
                x -= 1
        print(x)
# =========================================================================
        for i in operations:
            if i == "X++"or i == "++X":
                x += 1
            else:
                x -= 1
        print(x)
