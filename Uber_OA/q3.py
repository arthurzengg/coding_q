def solution(paragraphs, width):
    newspaper_page = []
    border = '*' * (width + 2)
    newspaper_page.append(border)

    for paragraph in paragraphs:
        current_line_words = []
        current_line_length = 0

        for chunk in paragraph:
            # Determine space needed before adding the next chunk
            space_needed = 1 if current_line_words else 0
            potential_length = current_line_length + space_needed + len(chunk)

            if potential_length <= width:
                current_line_words.append(chunk)
                current_line_length = potential_length
            else:
                # Process and add the current line
                line_text = ' '.join(current_line_words)
                line_length = len(line_text)
                leftover_space = width - line_length

                # Calculate spaces before and after the text
                spaces_before = leftover_space // 2
                spaces_after = leftover_space - spaces_before

                if leftover_space % 2 != 0:
                    # Add the extra space after the text
                    line = '*' + ' ' * spaces_before + line_text + ' ' * spaces_after + '*'
                else:
                    line = '*' + ' ' * spaces_before + line_text + ' ' * spaces_after + '*'

                newspaper_page.append(line)
                # Start a new line with the current chunk
                current_line_words = [chunk]
                current_line_length = len(chunk)

        # Add the last line of the paragraph if any words are left
        if current_line_words:
            line_text = ' '.join(current_line_words)
            line_length = len(line_text)
            leftover_space = width - line_length

            spaces_before = leftover_space // 2
            spaces_after = leftover_space - spaces_before

            if leftover_space % 2 != 0:
                line = '*' + ' ' * spaces_before + line_text + ' ' * spaces_after + '*'
            else:
                line = '*' + ' ' * spaces_before + line_text + ' ' * spaces_after + '*'

            newspaper_page.append(line)

    # Add the bottom border
    newspaper_page.append(border)
    return newspaper_page



print(solution([["hello", "world"], ["How", "areYou", "doing"], ["Please look",
"and align", "to center"]], 16))