#
# @lc app=leetcode id=787 lang=python
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
import collections
import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        min_heap = []
        heapq.heapify(min_heap)
        
        global res_price
        res_price = float("inf")
        
        # Holds the least price for each node
        # We don't care about lesser stops because worst case we are going to hit k, but better price is what we want
        details = {i: float("inf") for i in range(n)}
        
        # Creating adjacency list
        flights_dict = collections.defaultdict(list)
        
        for s, d, p in flights:
            flights_dict[s].append((d, p))
        
        # Heap: (Stops till now, price, node)
        heapq.heappush(min_heap, (-1, 0, src))
        
        # Visited set is not required here because we want to update iteratively
        # So same node can be updated multiple times to get the best min cost
        # But this will increase the runtime, so we need some checks to avoid redundant work
        
        # Unlike the network delay, where we have to maintain it because we pop based on least time always
        # So encountering the same node again means that the time must be greater than before.
        def bfs(dst, k):
            global res_price
            
            while min_heap:
                stops, price, node = heapq.heappop(min_heap)
                
                # To avoid adding same node unnecessarily
                details[node] = min(details[node], price)
    
                # Base case
                if node == dst and stops <= k:
                    res_price = min(res_price, price)
            
                for neighbor_node, price_to_neighbor in flights_dict[node]:
                    
                    # Only push the new node in heap, if it is offering a better price, we don't care about the stops as long as 1 + stops <= k
                    if price + price_to_neighbor <= details[neighbor_node] and 1 + stops <= k:
                        heapq.heappush(min_heap, (1 + stops, price + price_to_neighbor, neighbor_node))

            return res_price

        bfs(dst, k)

        if res_price == float("inf"):
            return -1
        
        return res_price
            
        
# @lc code=end

