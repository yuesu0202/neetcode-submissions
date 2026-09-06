class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(index, cur):
            if sum(cur) > target:
                return
            if sum(cur) == target:
                res.append(cur)
            for j in range(index, n):
                dfs(j, cur + [nums[j]])
        dfs(0, [])
        return res