class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        max_day = 0
        for i in range(len(jobs)):
            if workers[i] > jobs[i]:
                max_day = max(max_day, 1)
            else:
                if jobs[i] / workers[i] != jobs[i] // workers[i]:
                    max_day = max(max_day, jobs[i] // workers[i] + 1)
                else:
                    max_day = max(max_day, jobs[i] // workers[i])
        return max_day