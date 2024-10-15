def solution(arr):
    for i in range(0, len(arr) - 1, 2):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

print(solution([1,5,3,7,1,2]))
print(solution([6,7,8,8,5,3,2]))