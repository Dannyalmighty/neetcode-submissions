class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)      # userId -> list of (timestamp, tweetId)
        self.following = defaultdict(set)     # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1  # decrement so more recent tweets sort "smaller" (see note below)

    def getNewsFeed(self, userId: int) -> list[int]:
        max_heap = []

        # always include the user's own tweets, plus everyone they follow
        relevant_users = self.following[userId] | {userId}

        for uid in relevant_users:
            if self.tweets[uid]:
                # start from each user's MOST RECENT tweet (last in their list)
                index = len(self.tweets[uid]) - 1
                timestamp, tweetId = self.tweets[uid][index]
                heapq.heappush(max_heap, (timestamp, tweetId, uid, index - 1))

        result = []
        while max_heap and len(result) < 10:
            timestamp, tweetId, uid, index = heapq.heappop(max_heap)
            result.append(tweetId)

            if index >= 0:  # this user has more (older) tweets — push the next one
                next_timestamp, next_tweetId = self.tweets[uid][index]
                heapq.heappush(max_heap, (next_timestamp, next_tweetId, uid, index - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:  # a user doesn't need to "follow" themselves
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)