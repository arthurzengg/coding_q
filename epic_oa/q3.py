def finger_to_letters(finger_strokes):
    finger_mapping = {
        '1': ['v', 'f', 'r', 't', 'g', 'b'],
        '2': ['d', 'e', 'c'],
        '3': ['x', 's', 'w'],
        '4': ['z', 'a', 'q'],
        '6': ['m', 'j', 'u', 'y', 'h', 'n'],
        '7': ['k', 'i'],
        '8': ['l', 'o'],
        '9': ['p']
    }
    output = []
    for digit in finger_strokes:
        if digit in finger_mapping:
            output.append(finger_mapping[digit])
    return output

def generate_combinations(digits, index, current, output):
    if index == len(digits):
        output.append(''.join(current))
        return
    for letter in digits[index]:
        current.append(letter)
        generate_combinations(digits, index + 1, current, output)
        current.pop()

def list_possible_words(finger_strokes):
    letters = finger_to_letters(finger_strokes)
    if not letters:
        return []
    output = []
    generate_combinations(letters, 0, [], output)
    return output

# Example usage:
finger_strokes = "8801"
possibilities = list_possible_words(finger_strokes)
for possibility in possibilities:
    print(possibility)