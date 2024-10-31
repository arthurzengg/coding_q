class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_len = len(source)
        target_len = len(target)

        def find_sub(i, j):
            while i < source_len and j < target_len:
                if source[i] == target[j]:
                    j += 1
                    i += 1
                else:
                    i += 1
            return j

        ans = 0
        j = 0
        while j < target_len:
            new_target_index = find_sub(0, j)
            if new_target_index == j:
                return -1
            j = new_target_index
            ans += 1
        return ans
