from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        rem_dict = defaultdict(int)
        res = 0
        for num in time:
            num %= 60
            if num > 0:
                res += rem_dict[60 - num]
            else:
                res += rem_dict[num]

            rem_dict[num] = rem_dict[num] + 1

        return res

sol = Solution()
print(sol.numPairsDivisibleBy60([30,20,150,100,40]))
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60