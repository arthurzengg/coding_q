def solution(numbers):
    # Convert numbers to strings
    str_numbers = [str(num) for num in numbers]

    # Group numbers by length
    length_groups = {}
    for i, s in enumerate(str_numbers):
        length_groups.setdefault(len(s), []).append(s)

    def differ_by_one_digit(a, b):
        """Check if strings a and b differ by exactly one digit."""
        diff_count = 0
        for x, y in zip(a, b):
            if x != y:
                diff_count += 1
                if diff_count > 1:
                    return False
        return diff_count == 1

    total_pairs = 0
    # For each group of the same length, compare pairs
    for length, group in length_groups.items():
        # Compare each pair in the group
        n = len(group)
        for i in range(n):
            for j in range(i + 1, n):
                if differ_by_one_digit(group[i], group[j]):
                    total_pairs += 1

    return total_pairs


# ----- Example usage -----
if __name__ == "__main__":
    numbers = [1, 151, 241, 1, 9, 22, 351]
    print(solution(numbers))  # Expected output: 3
