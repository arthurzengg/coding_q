class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def display(root):
    lines, *_ = _display_aux(root)
    for line in lines:
        print(line)


def _display_aux(root):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if root.right is None and root.left is None:
        line = '%s' % root.value
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if root.right is None:
        lines, n, p, x = _display_aux(root.left)
        s = '%s' % root.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if root.left is None:
        lines, n, p, x = _display_aux(root.right)
        s = '%s' % root.value
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left_lines, n, p, x = _display_aux(root.left)
    right_lines, m, q, y = _display_aux(root.right)
    s = '%s' % root.value
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left_lines += [n * ' '] * (q - p)
    elif q < p:
        right_lines += [m * ' '] * (p - q)
    zipped_lines = zip(left_lines, right_lines)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


# Example usage:
if __name__ == '__main__':
    # Construct the binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.right.left = Node(8)
    root.right.right.right = Node(9)

    # Print the binary tree
    display(root)