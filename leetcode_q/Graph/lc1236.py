# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    """
    # 思路：
    1. 使用广度优先搜索（BFS）遍历所有可达的网页。
    2. 通过 HtmlParser 的 getUrls 方法获取当前网页的所有链接。
    3. 仅将属于同一主机名的网页加入到队列中继续爬取。
    4. 使用集合 visited 来记录已访问过的 URL，避免重复处理。

    方法：
    - get_hostname(url): 解析给定的 URL，提取并返回其主机名部分。
    - crawl(startUrl, htmlParser): 从 startUrl 开始，使用 htmlParser 接口抓取所有同主机名的网页。
    """

    def get_hostname(self, url):
        # 假设 URL 始终有效且以 http:// 或 https:// 开头
        # 找到 "://" 后面的内容开始的位置
        start = url.find('://') + 3
        # 找到主机名结束的位置（即第一个 '/' 的位置）
        end = url.find('/', start)
        # 如果 URL 中没有其他 '/', 则返回整个剩余字符串
        return url[start:end if end != -1 else None]

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited = set()
        queue = deque()
        queue.append(startUrl)
        visited.add(startUrl)
        hostname = self.get_hostname(startUrl)

        while queue:
            url = queue.popleft()
            for u in htmlParser.getUrls(url):
                if u not in visited and self.get_hostname(u) == hostname:
                    queue.append(u)
                    visited.add(u)

        return list(visited)

