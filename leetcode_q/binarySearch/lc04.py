class Solution:
    """
    # 思路：
    利用二分查找在两个有序数组中找到中位数。
    根据两个数组的总长度决定如何将它们分为两部分，使得：
    1. 左半部分的所有元素都小于或等于右半部分的所有元素。
    2. 左半部分和右半部分的元素数量相等（总数为偶数时）或左半部分比右半部分多一个元素（总数为奇数时）。

    通过对较短数组进行二分搜索，并使用中位数的性质确定在较长数组中的对应位置，从而达到 O(log(min(m,n))) 的时间复杂度。

    方法：
    - 找到两个数组中的较短数组进行二分搜索，以减少搜索空间，提高效率。
    - 计算应在左半部分的元素总数。
    - 根据二分搜索得到的索引计算出在较长数组中的对应索引。
    - 检查分割线左右的元素大小关系，确保左半部分的所有元素小于或等于右半部分的所有元素。
    - 根据数组总长度的奇偶性返回中位数。
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        # 确保对更短的数组进行二分搜索（提高效率）
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        # 总共要在“左半部分”放的元素个数
        # 若总长是奇数，会让左半比右半多一个
        totalLeft = (m + n + 1) // 2

        left, right = 0, m
        while left < right:
            # 取上中位数，这里相当于：
            # i 表示 nums1 左边拿多少个元素，j 表示 nums2 左边拿多少个元素，二者加起来恰好是 totalLeft
            # 也可以i = left + (right - left + 1) // 2
            i = (left + right + 1) // 2
            j = totalLeft - i

            # 如果 nums1[i-1] > nums2[j]，说明在 nums1 上切得太多了，需要往左收缩
            if i > 0 and nums1[i - 1] > nums2[j]:
                right = i - 1
            else:
                # 否则往右扩大
                left = i

        # 循环结束后，left == right，即在 nums1 上的切分点
        i = left
        j = totalLeft - i

        # 下面分别获取分割线左右两边的关键元素（可能越界，需特殊处理）
        nums1LeftMax = float('-inf') if i == 0 else nums1[i - 1]
        nums1RightMin = float('inf') if i == m else nums1[i]
        nums2LeftMax = float('-inf') if j == 0 else nums2[j - 1]
        nums2RightMin = float('inf') if j == n else nums2[j]

        # 如果总长度是奇数，中位数就是左半部分的最大值
        if (m + n) % 2 == 1:
            return max(nums1LeftMax, nums2LeftMax)
        else:
            # 偶数长度，取左右部分的“最大值”和“最小值”做平均
            return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2.0
