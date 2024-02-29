def validate_input(message):
    # Check if the message contains only letters and spaces
    return all(char.isalpha() or char.isspace() for char in message)

def square_code(message):
    # Validate the input string
    if not validate_input(message):
        return "Invalid input: Only letters and spaces are allowed."

    # Remove spaces from the message
    message = message.replace(" ", "").lower()

    # Calculate the size of the square
    length = len(message)
    columns = abs(int(length ** 0.5))

    # Create the square code
    encoded_message = []
    for i in range(columns):
        # Collect characters from each column
        column_message = message[i::columns]
        encoded_message.append(column_message)

    # Join the encoded message with spaces between columns
    return ' '.join(encoded_message)

# Example usage
message = "If on a winters night a traveler"
encoded_message = square_code(message)
print("Encoded message:", encoded_message)