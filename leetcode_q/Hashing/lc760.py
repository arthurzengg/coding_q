class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        res = []
        for i in range(len(nums2)):
            mapping[nums2[i]] = i
        for i in range(len(nums1)):
            res.append(mapping[nums1[i]])
        return res
