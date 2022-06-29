#
# @lc app=leetcode id=355 lang=python
#
# [355] Design Twitter
#

# @lc code=start
import collections

# Can be optimized using a max-heap which stores for each user, upon them or 
# their follower posting or their followers exisitng posts: 
# A tuple of (time, tweetID) limited to 10 elements.

class Twitter(object):

    def __init__(self):
        self.time = 0
        self.tweetIDs = collections.defaultdict(set)
        self.followers = collections.defaultdict(set)
        
    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweetIDs[userId].add((self.time, tweetId))
        self.time += 1
        
    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        self.allTweetsByAllFollowers = []
        self.final = []
        
        for tweetIDs_of_followers in self.followers[userId]:
            for tweet_time, tweetID in self.tweetIDs[tweetIDs_of_followers]:
                self.allTweetsByAllFollowers.append((tweet_time, tweetID))
        
        for self_tweet_time, self_tweetID in self.tweetIDs[userId]:
            self.allTweetsByAllFollowers.append((self_tweet_time, self_tweetID))
            
        self.final = sorted(self.allTweetsByAllFollowers, key=lambda x: x[0], reverse = True)
        
        return [x[1] for x in self.final][:10]

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

