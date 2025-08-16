class Solution:
    """
    题目要求判断数组中是否存在一个长度至少为 2 的连续子数组，
    使得子数组的和是 k 的倍数。

    核心思路：
    - 使用前缀和 + 同余定理。
    - 如果两个前缀和 pre[i]、pre[j] 对 k 取余相等，
      说明 nums[i+1..j] 的和可以被 k 整除。
    - 只需保证 j - i >= 2。

    实现方法：
    1. 用哈希表 d 存储余数第一次出现的位置，初始化 {0: -1}。
    2. 遍历数组，累加前缀和并取余 rem = pre % k。
    3. 如果余数 rem 没出现过，记录当前位置。
    4. 如果余数 rem 已出现过，并且 j - i >= 2，则返回 True。
    5. 遍历结束仍未找到，返回 False。

    举例：
    nums = [23, 2, 4, 6, 7], k = 6
    前缀和 mod 6 = [5, 1, 5, 5, 0]
    余数 5 出现过，且下标差 >= 2
    子数组 [2, 4] 和为 6，能被 6 整除 → 返回 True
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        pre = 0
        d = {0: -1}
        for index, num in enumerate(nums):
            pre += num
            rem = pre % k
            i = d.get(rem, index)
            if i == index:
                d[rem] = index
            elif i <= index - 2:
                return True

        return False