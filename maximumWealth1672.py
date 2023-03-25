class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = []
        for account in accounts:
            ans.append(sum(account))

        return max(ans)