class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(index, cur, total):
            if total == target:
                res.append(cur.copy())
            if total > target or index >= n:
                return
            
            for j in range(index, n):
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        dfs(0, [], 0)
        return res     