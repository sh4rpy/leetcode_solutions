class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        i = 0
        n = len(s)
        ans = ['-'] * n
        while i < n:
            ans[indices[i]] = s[i]
            i += 1
        return ''.join(ans)
