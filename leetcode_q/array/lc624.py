class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minVal = arrays[0][0]
        maxVal = arrays[0][-1]
        result = 0
        for i in range(1, len(arrays)):
            result = max(result, max(abs(arrays[i][-1] - minVal), abs(arrays[i][0] - maxVal)))
            minVal = min(minVal, arrays[i][0])
            maxVal = max(maxVal, arrays[i][-1])
        return result