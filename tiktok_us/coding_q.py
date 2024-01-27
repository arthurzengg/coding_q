# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# [2,1,1]
# [1,1,0]
# [0,1,1]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# [2,1,1]
# [0,1,1]
# [1,0,1]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

from collections import deque


def solve(grid):
    rows, cols = len(grid), len(grid[0])
    fresh = 0
    rotten = deque()
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                fresh += 1
            if grid[row][col] == 2:
                rotten.append((row, col))

    # print(rotten)
    print("before ", fresh)
    minutes = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while rotten and fresh > 0:
        minutes += 1
        for _ in range(len(rotten)):
            r, c = rotten.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    rotten.append((nr, nc))
                    # print(grid)
    if fresh == 0:
        return minutes
    else:
        print(fresh)
        return -1


# gird = [[2,1,1],[1,1,0],[0,1,1]]
# print(solve(gird))
# [2,1,1]
# [1,1,0]
# [0,1,1]

# rotten = [(0, 0)]
# r = 0
# c = 0

# rotten = [(0, 1), (1, 0)]
# r = 0
# c = 1


# You are given a list of songs where the ith song has a duration of time[i] seconds.

# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.


# Example 1:
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60

# Example 2:
# Input: time = [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.


# (time[i] + time[j]) = 60
# [30,20, 20,80,150,100,40]


def solve_p2(time):
    res = 0
    remainder_count = {}

    for t in time:
        # t%60 remainder, complement + ramainder = 60
        # complement = -t % 60
        remainder = t % 60

        target = (60 - remainder) % 60

        res += remainder_count.get(target, 0)

        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

    return res


time = [60, 60, 60]
# (30, 150),
print(solve_p2(time))













