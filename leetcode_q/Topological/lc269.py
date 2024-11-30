class Solution:
    """
    此解法用于根据给定的单词列表推断外星语言的字母顺序。
    思路：
    1. 初始化每个出现的字符的入度为0，并建立一个有向图来表示字符间的顺序关系。
    2. 遍历单词列表，比较相邻两个单词，找到第一对不同的字符，建立前一个字符指向后一个字符的边，并更新后一个字符的入度。
    3. 如果在比较过程中没有找到不同字符且前一个单词长度大于后一个单词，说明输入无效，直接返回空字符串。
    4. 使用拓扑排序（基于队列）来确定字符的顺序。入度为0的字符可以加入队列和结果列表。
    5. 从队列中依次取出字符，将其指向的字符的入度减1，如果减后入度为0，则将其加入队列。
    6. 如果最终结果列表的长度与图中节点的数量相同，返回结果字符串，否则返回空字符串表示存在循环依赖，无法确定完整顺序。

    方法：
    - alienOrder(self, words): 主函数，输入单词列表，输出字符顺序或空字符串。
    """

    def alienOrder(self, words):
        res = []
        in_degree = defaultdict(int)
        graph = defaultdict(list)

        for word in words:
            for char in word:
                in_degree[char] = 0
        in_degree = {char: 0 for word in words for char in word}

        for i in range(1, len(words)):
            pre = words[i - 1]
            current = words[i]
            index = 0
            found_difference = False
            while index < len(pre) and index < len(current):
                p = pre[index]
                c = current[index]
                if p != c:
                    if p not in graph:
                        graph[p] = []
                    if c not in graph[p]:
                        graph[p].append(c)
                        in_degree[c] += 1
                    found_difference = True
                    break
                index += 1
            if not found_difference and len(pre) > len(current):
                return ""  # 处理无效情况

        print(graph)
        print(in_degree)
        queue = deque()
        for key, value in in_degree.items():
            if value == 0:
                queue.append(key)
                res.append(key)

        while queue:
            cur_queue = queue
            for _ in range(len(cur_queue)):
                node = cur_queue.popleft()
                if graph[node]:
                    for edge in graph[node]:
                        in_degree[edge] -= 1
                        if in_degree[edge] == 0:
                            res.append(edge)
                            cur_queue.append(edge)
            queue = cur_queue

        if len(res) == len(in_degree):
            return ''.join(res)
        return ""  # 存在循环，无法进行有效的拓扑排序 ["z","x","a","zb","zx"]
