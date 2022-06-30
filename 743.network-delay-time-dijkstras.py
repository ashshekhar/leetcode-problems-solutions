#
# @lc app=leetcode id=743 lang=python
#
# [743] Network Delay Time
#

# @lc code=start
import collections
import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        min_heap = []
        heapq.heapify(min_heap)
        
        visited = set()
        
        global time
        time = 0
        
        # Preparing the adjacency list
        network = collections.defaultdict(list)
        
        for src, dest, weight in times:
            network[src].append((weight, dest))
        
        # Pushing in the source node
        # Heap push based on the weight - extract lowest weight element in O(1)
        heapq.heappush(min_heap, (0, k))
        
        # Djikstra's - BFS using min-heap
        def bfs():
            global time

            while min_heap:
                current_weight, current_node = heapq.heappop(min_heap)

                # Continue if we encounter a visited node because this is the second heap item with the same node but with more price / stops
                if current_node in visited:
                    continue
                else:
                    visited.add(current_node)
                    
                time = max(time, current_weight)
                
                for neighbor_weight, neighbor_node in network[current_node]:
                    
                    # Since you're doing a while loop, duplicate nodes will also be popped, but
                    # we only need to update their time once as we are using min_heap, so skip
                    if neighbor_node not in visited:
                        heapq.heappush(min_heap, (current_weight + neighbor_weight, neighbor_node))
            
            return time

        bfs()
        return time if len(visited) == n else -1
    
# @lc code=end

