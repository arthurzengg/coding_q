class TrieNode:
    """表示前缀树的节点，用于模拟文件系统中的目录或文件。"""

    def __init__(self, name):
        self.name = name  # 节点名称
        self.content = ''  # 文件内容
        self.isFile = False  # 是否是文件
        self.next = defaultdict(TrieNode)  # 子节点


class FileSystem:
    """
    # 思路：
    1. 使用前缀树（Trie）来管理文件和目录的层次结构。
    2. 每个节点代表一个文件或目录，节点存储名称、内容、类型（文件/目录）和子节点的引用。
    3. 提供基本文件操作：
       - ls: 列出目录的内容或返回文件名。
       - mkdir: 创建目录。
       - addContentToFile: 向文件添加内容。
       - readContentFromFile: 读取文件内容。
    4. 通过字符串路径管理文件系统中的文件和目录。
    """

    def __init__(self):
        self.head = TrieNode('')  # 创建根节点

    def ls(self, path: str) -> List[str]:
        cur = self.find_path(path)
        if cur.isFile:
            return [cur.name]  # 如果是文件，返回文件名
        res = []
        for p in cur.next:
            res.append(p)  # 如果是目录，返回目录内容
        return sorted(res)

    def mkdir(self, path: str) -> None:
        self.find_path(path)  # 创建路径中的所有目录

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.find_path(filePath)
        cur.isFile = True  # 标记为文件
        cur.content += content  # 追加内容

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.find_path(filePath)
        return cur.content  # 返回文件内容

    def find_path(self, path):
        cur = self.head
        if path == '/':
            return cur
        paths = path.split('/')[1:]  # 跳过空字符
        for p in paths:
            if p not in cur.next:
                cur.next[p] = TrieNode(p)  # 创建新节点
            cur = cur.next[p]
        return cur