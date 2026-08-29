class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        def dfs(index, parts):
            if len(parts) == 4:
                if index == n:
                    ans.append(".".join(parts))
                return
            if index >= n:
                return
            if s[index] == '0':
                parts.append('0')
                dfs(index + 1, parts)
                parts.pop()
            else:
                for i in range(1,4):
                    part = s[index:index+i]
                    if int(part) > 255:
                        continue
                    parts.append(part)
                    dfs(index+i, parts)
                    parts.pop()
        dfs(0, [])
        return ans