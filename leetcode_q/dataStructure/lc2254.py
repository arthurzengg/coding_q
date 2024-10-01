class Video:
    def __init__(self, content):
        self.content = content
        self.content_length = 0
        self.like = 0
        self.dislike = 0
        self.view = 0


class VideoSharingPlatform:

    def __init__(self):
        self.nextId = 0
        self.db = {}
        self.availableIds = []

    def upload(self, video: str) -> int:
        if self.availableIds:
            videoId = self.availableIds.pop(0)
        else:
            videoId = self.nextId
            self.nextId += 1
        self.db[videoId] = Video(video)
        self.db[videoId].content_length = len(video)
        return videoId

    def remove(self, videoId: int) -> None:
        if videoId in self.db:
            self.db[videoId] = Video('')
            self.availableIds.append(videoId)
            self.availableIds.sort()

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId in self.db:
            self.db[videoId].view += 1
            return self.db[videoId].content[startMinute: min(endMinute + 1, self.db[videoId].content_length)]
        return "-1"

    def like(self, videoId: int) -> None:
        if videoId in self.db:
            self.db[videoId].like += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.db:
            self.db[videoId].dislike += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId in self.db:
            return [self.db[videoId].like, self.db[videoId].dislike]
        return [-1]

    def getViews(self, videoId: int) -> int:
        if videoId in self.db:
            return self.db[videoId].view
        return -1

# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)