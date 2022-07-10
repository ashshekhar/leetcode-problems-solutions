# First create an updated Trie from the inputs, then find the diameter of the Trie

class TrieNode(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.endOfWord = False

def find_max_distance(input):
    root = TrieNode()

    for binary in input:
        current = root
        
        for char in binary:
          
            # Append left for 0
            if char == '0':
                if not current.left:
                    current.left = TrieNode()
                current = current.left

            # Append right for 1
            else:
                if not current.right:
                    current.right = TrieNode()
                current = current.right

        current.endOfWord = True

    global diameter
    diameter = 0
    
    find_diameter(root)
    return diameter

def find_diameter(node):
    global diameter
    
    if not node:
        return 0, 0
    
    left_subtree_sum, left_subtree_height = find_diameter(node.left)
    right_subtree_sum, right_subtree_height = find_diameter(node.right)
    
    # Add the heights at point of split, or end of word
    if node.endOfWord or (node.left and node.right):
        diameter = max(diameter, left_subtree_height + right_subtree_height)
    
    # Otherwise the diameter will simply be the max sum
    else:
        diameter = max(left_subtree_sum, right_subtree_sum)

    return diameter, 1 + max(left_subtree_height, right_subtree_height)
    
input_arr = ["101", "10100"]
print(find_max_distance(input_arr))