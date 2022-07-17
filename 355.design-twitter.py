#
# @lc app=leetcode id=355 lang=python
#
# [355] Design Twitter
#

# @lc code=start
import collections

# Can be optimized using a max-heap which stores for each user, 
# A tuple of (time, tweetID) limited to 10 elements.

class Twitter(object):

    def __init__(self):
        self.time = 0
        
        # Maps userID -> (time, tweetID by userID)
        self.tweetIDs = collections.defaultdict(set)
        
        # Maps followerID -> followeeID
        # So mapping each userID to all their followings
        self.followers = collections.defaultdict(set)
        
    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweetIDs[userId].add((self.time, tweetId))
        self.time += 1

    # Find top 10 tweets by followees and user itself based on time
    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        self.allTweetsByAllFollowers = []
        self.final = []
        
        # Find all posts by the followees of userID
        for tweetIDs_of_followees in self.followers[userId]:
            
            # Find all tweets by each followee
            for tweet_time, tweetID in self.tweetIDs[tweetIDs_of_followees]:
                self.allTweetsByAllFollowers.append((tweet_time, tweetID))
        
        # Next, also find all the posts by userID itself
        for self_tweet_time, self_tweetID in self.tweetIDs[userId]:
            self.allTweetsByAllFollowers.append((self_tweet_time, self_tweetID))
        
        # Sort all the tweets by post time in reverse order
        # Latest posts on top
        self.allTweetsByAllFollowers = sorted(self.allTweetsByAllFollowers, key=lambda x: x[0], reverse = True)
        
        # Retreive the tweetIDs of top 10 based on time
        return [x[1] for x in self.allTweetsByAllFollowers][:10]

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

