def solution(numbers, zerosToOne):
    num_ones = numbers.count(1)
    num_zeros = numbers.count(0)
    time = 0

    while True:
        # Option 1: Convert zeros to one
        while num_zeros >= zerosToOne:
            num_zeros -= zerosToOne
            num_ones += 1
            time += 1

        # Option 2: Change last one to zero
        while num_ones >= 1:
            num_ones -= 1
            num_zeros += 1
            time += 1
            # Check if we can perform Option 1 again
            if num_zeros >= zerosToOne:
                break  # Go back to Option 1

        # If neither option can be performed, halt the process
        if num_zeros < zerosToOne and num_ones == 0:
            break

    return time

print(solution([1,1,1,0,0,0],2))
print(solution([1,1],2))
print(solution([0,0,0],3))