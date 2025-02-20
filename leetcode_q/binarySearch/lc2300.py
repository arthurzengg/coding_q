from typing import List


class Solution:
    """
    中文思路解析：
    1. 首先对药水数组进行排序，以便后续进行二分查找。
    2. 遍历每个咒语，对于每个咒语：
       - 计算为了达到成功阈值至少需要的药水强度。这是通过将成功阈值除以咒语值并向上取整得到的。
       - 使用二分查找确定这个最小药水强度在排序后的药水数组中的位置。找到的位置表明所有更强的药水都能与当前咒语成功组合。
       - 计算出所有能与当前咒语成功组合的药水数量，并将这个数量加入到结果列表中。
    3. 特别注意边界情况：
       - 如果计算得到的最小药水强度大于所有药水，说明没有任何一个药水可以与这个咒语成功组合。
       - 如果最小药水强度小于等于药水数组中的最小值，说明所有药水都可以与这个咒语成功组合。

    关键点：
    - 排序药水数组使得可以通过二分查找快速确定满足条件的药水范围。
    - 二分查找帮助快速定位到第一个满足条件的药水，从而可以直接计算出满足条件的药水数量。
    - 对于每个咒语，该算法都能以对数时间复杂度找到答案，提高了整体效率。
    """

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        res = []
        for spell in spells:
            # 计算需要的最小药水强度
            if success % spell == 0:
                num_needed = success // spell
            else:
                num_needed = success // spell + 1

            # 通过二分查找定位药水强度的下界
            if num_needed > potions[-1]:
                res.append(0)
                continue
            elif num_needed < potions[0]:
                res.append(len(potions))
                continue
            left = 0
            right = len(potions) - 1
            while left < right:
                mid = (left + right) // 2
                if potions[mid] >= num_needed:
                    right = mid
                else:
                    left = mid + 1
            res.append(len(potions) - left)
        return res