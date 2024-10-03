class Leaderboard:

    def __init__(self):
        self.leaderboard = {}
        self.scoreList = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.leaderboard:
            old_score = self.leaderboard[playerId]
            self.scoreList.remove(old_score)
            self.leaderboard[playerId] = old_score + score
        else:
            self.leaderboard[playerId] = score
        left, right = 0, len(self.scoreList)
        while left < right:
            mid = (left + right) // 2
            if self.scoreList[mid] >= self.leaderboard[playerId]:
                left = mid + 1
            else:
                right = mid
        self.scoreList.insert(left, self.leaderboard[playerId])

    def top(self, K: int) -> int:
        res = 0
        for i in range(K):
            res += self.scoreList[i]
        return res

    def reset(self, playerId: int) -> None:
        scoreRem = self.leaderboard[playerId]
        self.leaderboard.pop(playerId)
        self.scoreList.remove(scoreRem)
