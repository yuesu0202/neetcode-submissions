# class Solution:
#     def restoreIpAddresses(self, s: str) -> List[str]:
#         n = len(s)
#         ans = []
#         def dfs(index, parts):
#             if len(parts) == 4:
#                 if index == n:
#                     ans.append(".".join(parts))
#                 return
#             if index >= n:
#                 return
#             if s[index] == '0':
#                 parts.append('0')
#                 dfs(index + 1, parts)
#                 parts.pop()
#             else:
#                 for i in range(1,4):
#                     part = s[index:index+i]
#                     if int(part) > 255:
#                         continue
#                     parts.append(part)
#                     dfs(index+i, parts)
#                     parts.pop()
#         dfs(0, [])
#         return ans


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []


        def dfs(i, k, curIP):
            if k == 4 and i == n:
                res.append(curIP[:-1])
                return
            if k > 4 or i >= n:
                return
            for j in range(i, min(i+3, len(s))):
                if i != j and s[i] == '0':
                    continue
                if int(s[i:j+1]) < 256:
                    dfs(j+1, k+1, curIP + s[i:j+1] + '.')
        dfs(0, 0, "")
        return res