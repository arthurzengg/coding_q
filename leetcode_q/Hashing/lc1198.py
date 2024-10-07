class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        mapping = defaultdict(int)
        for array in mat:
            for num in array:
                mapping[num] += 1
        for key, value in mapping.items():
            if mapping[key] == len(mat):
                return key
        return -1

