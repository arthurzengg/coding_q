class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        path = []

        def backtracking(path, startIndex):
            if sum(path) == target:
                res.append(path[:])
            if sum(path) > target:
                return
            for i in range(startIndex, len(candidates)):
                path.append(candidates[i])
                backtracking(path, i)
                path.pop()

        backtracking(path, 0)
        return res


sol = Solution()
candidates = [2,3,6,7]
target = 7
print(sol.combinationSum(candidates, target)) #Output:[[2, 2, 3], [7]]