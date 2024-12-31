class Solution:
    """
    思路：
    1. 创建一个字典 hashmap 来存储元素及其最近一次出现的索引。
    2. 遍历数组 nums，对于每个元素：
       - 如果元素不在 hashmap 中，记录它的索引。
       - 如果元素已存在于 hashmap 中，比较当前索引 i 与 hashmap 中记录的索引的差值：
         - 如果差值小于等于 k，则找到了符合条件的一对，返回 True。
         - 如果差值大于 k，则更新该元素的索引为当前索引 i，以便于后续的比较。
    3. 遍历完成后，如果没有找到任何符合条件的索引对，返回 False。
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                if abs(hashmap[nums[i]] - i) <= k:
                    return True
                else:
                    hashmap[nums[i]] = i
        return False
