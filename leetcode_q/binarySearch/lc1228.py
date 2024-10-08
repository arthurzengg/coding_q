class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n
        diff = (arr[-1] - arr[0]) / n
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == arr[0] + diff * mid:
                left = mid + 1
            else:
                right = mid
        return int(arr[0] + left * diff)
