def getTotalImpact(initialReelImpacts, newReelImpacts, k):
    import heapq

    # Initialize heap with k largest elements from initialReelImpacts
    initialReelImpacts.sort(reverse=True)
    heap = []
    total_reels = len(initialReelImpacts)
    for impact in initialReelImpacts[:k]:
        heapq.heappush(heap, impact)

    # Initialize total impact score
    if total_reels >= k:
        impact_score = heap[0]
    else:
        impact_score = 0

    # Process each day
    for new_impact in newReelImpacts:
        total_reels += 1
        if len(heap) < k:
            heapq.heappush(heap, new_impact)
        else:
            if new_impact > heap[0]:
                heapq.heapreplace(heap, new_impact)
        if total_reels >= k:
            impact_score += heap[0]

    return impact_score

initialReelImpacts = [2,2,4]
newReelImpacts = [3,3,5]
k = 2
print(getTotalImpact(initialReelImpacts, newReelImpacts, k))

initialReelImpacts = [2,3,4]
newReelImpacts = [7,6,5]
k = 1
print(getTotalImpact(initialReelImpacts, newReelImpacts, k))


# In the dynamic landscape of TikTok, creators are in a constant race to boost their videos' engagement and reach by leveraging new features that enhance their content.
# Each creator starts with a set of m videos represented by initia/Reellmpacts, which indicates the baseline popularity of each reel. For next n days, TikTok releases new trending features represented by newReellmpacts, with each feature offering an additional boost to the creator's existing reels.
# On each of the next n days, the following takes place:
# • The creator appends the new features represented by newReellmpacts[i (where 0 ≤ i < n) to their current reels
# • Review the updated lineup, select the kth most impactful reel based on its popularity, and add its impact value to their total impact score
# For example, if k = 1, the creator selects the reel with the highest popularity; if k = 2, the creator selects the reel with the second highest popularity, and so on.
#
# Given two integer arrays, initialReelImpacts and newReellmpacts of length m and n respectively and an integer k. The task is to calculate the creator's total impact score after incorporating all elements from newReellmpacts across n days.
# Note: The initial impact score of the creator is considered to be the kth highest impact value from the initia set of initia/Reellmpacts.
# Example
# m = 2
# initialReelImpacts = [2, 3]
# n= 3
# newReellmpacts = [4, 5, 1]
# K = 2
# The initial impact score of the creator is 2nd highest impact value from the initial set of initialReellmpacts = [2, 3]. Thus, impact score = 2.
#
# Over the next n days the following process unfolds:
# Index (i) newReellmpacts[i] current reels impact sorted order of reels kth-highest impact score
# 0 4 [2, 3, 4] [2, 3, 4] 3 2 + 3=5
# 1 5 [2, 3, 4, 5] [2, 3, 4, 5] 4 5 + 4 =9
# 2 1 [2, 3, 4, 5,1] [1, 2, 3, 4, 5] 4 9 + 4 = 13
# • Day 1: The creator appends a new reel with an impact of 4, resulting in [2, 3, 4], and selects the 2nd highest impact of 3, making impact score 2 + 3 = 5.
# • Day 2: The creator appends a new reel with an impact of 5, resulting in [2, 3, 4, 5], and selects the 2nd highest impact of 4, bringing total impact score to 5 + 4 = 9.
# • Day 3: The creator appends a new reel with an impact of 1, resulting in [1, 2, 3, 4, 5], and selects the 2nd highest impact of 4, making total impact score to 9 + 4 = 13.
# Therefore the creator's total impact score after incorporating all elements from newReellmpacts across given n days is 13.
# Hence return 13 as the answer.
# Function Description
# Complete the function getTotallmpact in the editor below.
# getTotallmpact has the following parameter(s):
# int initia/ReelImpacts[m]: The impact of initial m reels
# int newReellmpacts[n]: The impact of the new n reels that appear one by one
# int k. The fixed choice made by the creator, representing the position of the most impactful reel selecte
# Returns
# long: The total impact achieved by the creator after incorporating all elements from newReelImpacts.
#
# def getTotalImpact(initialReelImpacts, newRellImpacts, k):