def getDistanceMetrics(arr):
    from collections import defaultdict

    n = len(arr)
    res = [0] * n

    value_to_indices = defaultdict(list)
    for idx, val in enumerate(arr):
        value_to_indices[val].append(idx)

    for indices in value_to_indices.values():
        k = len(indices)
        if k == 1:
            res[indices[0]] = 0
            continue

        cumSum = [0] * k
        cumSum[0] = indices[0]
        for j in range(1, k):
            cumSum[j] = cumSum[j - 1] + indices[j]

        total_cumSum = cumSum[-1]

        for i in range(k):
            idx_i = indices[i]
            idx_val = indices[i]
            if i > 0:
                sum_left = idx_val * i - cumSum[i - 1]
            else:
                sum_left = 0

            if i < k - 1:
                sum_right = (cumSum[k - 1] - cumSum[i]) - idx_val * (k - i - 1)
            else:
                sum_right = 0

            total_sum = sum_left + sum_right
            res[idx_i] = total_sum

    return res

print(getDistanceMetrics([1,2,1,1,2,3]))
print(getDistanceMetrics([99,99,99,2999,2999,2999]))