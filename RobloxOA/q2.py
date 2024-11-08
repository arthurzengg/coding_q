def solution(a, b, queries):
    from collections import Counter
    a_counter = Counter(a)
    b_counter = Counter(b)
    result = []

    for query in queries:
        if query[0] == 0:
            # Update b[i] += x
            i = query[1]
            x = query[2]
            old_value = b[i]
            b_counter[old_value] -= 1
            if b_counter[old_value] == 0:
                del b_counter[old_value]
            b[i] += x
            new_value = b[i]
            b_counter[new_value] += 1
        elif query[0] == 1:
            x = query[1]
            total = 0
            for val_a, count_a in a_counter.items():
                val_b = x - val_a
                count_b = b_counter.get(val_b, 0)
                total += count_a * count_b
            result.append(total)
    return result

a = [1,2,3]
b=[1,4]
queries =  [[1, 5], [0, 0, 2], [1, 5]]
print(solution(a,b,queries))

a = [1, 2, 2]
b = [2, 3]
queries = [[1, 4], [0, 0, 1], [1, 5]]
print(solution(a,b,queries))