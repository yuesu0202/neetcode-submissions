class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direction = [[1,0], [-1,0], [0,1], [0,-1]]

        def invalid(r,c):
            return r < 0 or c < 0 or r >= N or c >= N
        
        visit = set()
        def dfs(r, c):
            if (invalid(r, c) or not grid[r][c] or (r, c) in visit):
                return
            visit.add((r, c))
            for dr, dc in direction:
                dfs(r + dr, c + dc)
        
        def bfs():
            res, q = 0, deque(visit)
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direction:
                        curR, curC = r + dr, c + dc
                        if invalid(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC]:
                            return res
                        visit.add((curR, curC))
                        q.append((curR, curC))
                res += 1
        

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()