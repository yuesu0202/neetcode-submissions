class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        # visited = set()
        def dfs(index, cur, total):
            if total == target:
                # visited.add(tuple(cur))
                res.append(cur.copy())
                return
            if total > target or index >= len(candidates):
                return
            
            for j in range(index, len(candidates)):
                cur.append(candidates[j])
                if j == index or candidates[j] != candidates[j-1]:
                # if tuple(cur) not in visited:
                    dfs(j+1, cur, total + candidates[j])
                cur.pop()
        dfs(0, [], 0)
        return res
                