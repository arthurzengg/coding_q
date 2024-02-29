def find_sum_seeds(number):
    sum_seeds = []

    # Function to calculate the sum of digits of a number
    def digit_sum(n):
        total = 0
        # Loop through each digit of the number
        while n > 0:
            # Extract the last digit
            digit = n % 10
            # Add the digit to the total sum
            total += digit
            # Remove the last digit from the number
            n //= 10
        return total

    # Check for sum seeds
    for i in range(1, number):
        # Calculate the sum of the current number and the sum of its digits
        current_sum = i + digit_sum(i)
        # If the sum matches the input number, add the current number to sum_seeds
        if current_sum == number:
            sum_seeds.append(i)

    return sum_seeds

print(find_sum_seeds(256))