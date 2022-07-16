from collections import OrderedDict
from itertools import combinations
import collections

class Solution(object):    
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        # Maps user name to websites they visited
        input_dictionary = collections.defaultdict(list)
        
        # Maps all possible patterns (using combinations) to thier count
        pattern_dict = collections.defaultdict(int)
        
        # Sort the input based on the timestamp
        sorted_list = sorted(zip(username, website, timestamp), key = lambda x:x[2])
        
        # Read input dictionary properly
        for user, web, time in sorted_list:
            input_dictionary[user].append(web)
        
        # Create a dictionary for patterns
        for key, values in input_dictionary.items():
            returned_list = sorted(set(combinations(values, 3)))

            for items in returned_list:
                pattern_dict[tuple(items)] += 1

        # Sort first by frequency / count
        # then by the item / pattern itself for lexicographical order
        def sortKey(key):
            return (-pattern_dict[key], key)

        return sorted(pattern_dict, key = sortKey)[0]