class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        # Dictionary to hold the count of remainders
        remainder_count = {}
        # Initialize the number of pairs to zero
        num_pairs = 0

        for t in time:
            # Calculate the complement that would sum with the current time to be divisible by 60
            complement = -t % 60
            # If the complement is in the dictionary, add the count of the complement to the number of pairs
            num_pairs += remainder_count.get(complement, 0)
            # Add the current remainder count to the dictionary
            remainder_count[t % 60] = remainder_count.get(t % 60, 0) + 1

        return num_pairs

sol = Solution()
print(sol.numPairsDivisibleBy60([30,20,150,100,40]))
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60