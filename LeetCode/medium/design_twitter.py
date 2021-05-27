"""
Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.


Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.


Constraints:

1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 104
All the tweets have unique IDs.
At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.

"""


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followers = defaultdict(set)  # userId --> set of her followers
        self.followees = defaultdict(set)  # userId --> set of people she follows
        self.feeds = defaultdict(lambda: [])  # userId --> maxHeap of her tweets plus tweets from her followees
        self.numTweets = 0  # total number of tweets in this instantiation of Twitter()
        self.tweetOrder = {}  # tweet index --> tweetId. First tweet ever has index 0
        self.author = defaultdict(lambda: [])  # user Id --> list of tweet indices she has authored

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweetOrder[self.numTweets] = tweetId
        heapq.heappush(self.feeds[userId], self.numTweets)
        for follower in self.followers[userId]:
            heapq.heappush(self.feeds[follower], self.numTweets)
        self.author[userId].append(self.numTweets)
        self.numTweets += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        return [self.tweetOrder[tweetIndex] for tweetIndex in heapq.nlargest(10, self.feeds[userId])]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.followees[followerId]:
            for tweetIndex in self.author[followeeId]:
                heapq.heappush(self.feeds[followerId], tweetIndex)
        self.followers[followeeId].add(followerId)
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.followees[followerId]:
            for tweetIndex in self.author[followeeId]:
                self.feeds[followerId].remove(tweetIndex)
                heapq.heapify(self.feeds[followerId])
        self.followers[followeeId].discard(followeeId)
        self.followees[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)