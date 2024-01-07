class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findCommonAncestor(root, p, q):
            if not root:
                return None
            if root.val == p or root.val == q:
                return root
            left = findCommonAncestor(root.left, p, q)
            right = findCommonAncestor(root.right, p, q)
            if left and not right:
                return left
            elif not left and right:
                return right
            elif not left and not right:
                return None
            else:
                return root

        commonAncestor = findCommonAncestor(root, startValue, destValue)

        path_start = 0
        path_dest = ''
        queue = []
        queue.append((commonAncestor, ''))
        while queue:
            temp = queue.pop(0)
            node, path = temp[0], temp[1]
            if node.val ==  startValue:
                path_start = len(path)
            elif node.val == destValue:
                path_dest = path
            if node.left:
                queue.append((node.left, path + 'L'))
            if node.right:
                queue.append((node.right, path + 'R'))

        return path_start * 'U' + path_dest