#
# @lc app=leetcode id=535 lang=python
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
class Codec:
    def __init__(self):
        # Stores the encoded URLs
        self.encodeMap = {}
        
        # Maps the encoded URLs to decoded URLs
        self.decodeMap = {}
        
        # To append to
        self.baseURL = "http://tinyurl.com/"
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.encodeMap:
            return self.encodeMap[longUrl]
        
        # The shortenedURL is basically the base + number of length of map 
        shortUrl = self.baseURL + str(1 + len(self.encodeMap))
        
        self.encodeMap[longUrl] = shortUrl
        self.decodeMap[shortUrl] = longUrl
        
        return self.encodeMap[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.decodeMap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

