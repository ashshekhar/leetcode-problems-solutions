#
# @lc app=leetcode id=692 lang=python
#
# [692] Top K Frequent Words
#

# @lc code=start
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        heap = []
        dictionary = {}
        
        for word in words:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1

        for key, value in dictionary.items():
            heapq.heappush(heap, ( -1 * value, key))
        
        return [x[1] for x in heapq.nsmallest(k, heap)]
# @lc code=end

