class TweetCounts:

    def __init__(self):
        self.maps = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        # dictionary of list
        self.maps[tweetName].append(time)


    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        chunk_size = {"minute": 60, "hour":3600, "day":86400}
        rslt = [0]*((endTime-startTime)//chunk_size[freq]+1)
        for time in self.maps[tweetName]:
            if startTime <= time <= endTime:
                rslt[(time-startTime)//chunk_size[freq]] +=1
        return rslt
