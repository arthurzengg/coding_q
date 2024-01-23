class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        n = len(heights)
        res = []
        max_height = float('-inf')
        for i in range(n - 1, -1, -1):
            if heights[i] > max_height:
                max_height = heights[i]
                res.append(i)
        res.sort()
        return res

sol = Solution()
print(sol.findBuildings([4,2,3,1]))
# Output [0,2,3]
print(sol.findBuildings([4,3,2,1]))
# Output [0,1,2,3]