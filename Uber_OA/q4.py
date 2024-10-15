def solution(operations):
    max_min_side = 0
    max_max_side = 0
    result = []
    for op in operations:
        if op[0] == 0:
            # Save rectangle
            min_side = min(op[1], op[2])
            max_side = max(op[1], op[2])
            max_min_side = max(max_min_side, min_side)
            max_max_side = max(max_max_side, max_side)
        elif op[0] == 1:
            # Query
            box_min = min(op[1], op[2])
            box_max = max(op[1], op[2])
            if max_min_side <= box_min and max_max_side <= box_max:
                result.append(True)
            else:
                result.append(False)
    return result


print(solution([[0, 1, 3], [0, 4, 2], [1, 3, 4], [1, 3, 2]]))
