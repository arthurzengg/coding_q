class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        if n == 1:
            return s
        for direction, step in shift:
            step = step % n
            if step == 0:
                continue
            if direction == 0:
                left = s[:step]
                s = s[step:] + left
            else:
                right = s[n - step:]
                s = right + s[:n - step]
        return s


