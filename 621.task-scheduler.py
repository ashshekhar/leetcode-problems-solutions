#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#

# @lc code=start
from collections import deque, Counter
import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)
        
        queue = deque()
        time = 0
        count = Counter(tasks)
        tasks_new = []
        
        # Use of max heap and queue data structures
        tasks_new = [-1 * count[keys] for keys in count.keys()]
        heapq.heapify(tasks_new)
        
        while tasks_new or queue:
            
            # Important to increase time on entering to keep processing either data structures          
            time += 1

            # Process the most frequent tasks
            if tasks_new:
                process = heapq.heappop(tasks_new)
                if process + 1 != 0:
                    queue.append([process + 1, time + n])
            
            # Also keep track of the time and append old tasks in heap to process when okay to process
            if queue and time == queue[0][1]:
                heapq.heappush(tasks_new, queue.popleft()[0])
        
        return time
        
        
# @lc code=end

