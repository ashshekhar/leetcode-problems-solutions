from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.content = ""
        
        
class FileSystem(object):
    def __init__(self):
        self.root = TrieNode()

    # Find / Create the nodes in path and return last node
    def find(self, path, create = False):
        cur = self.root
        
        if len(path) == 1:
            return cur
        
        for word in path.split('/')[1:]:
            if not cur.children.get(word) and not create:
                return None
    
            cur = cur.children[word]
            
        return cur
    
    # List file name if path is a file path
    # else list all files and directories inside the directory path
    def ls(self, path):
        curr = self.find(path)
        
        # Input is a file path, return file name
        if curr.content:
            return [path.split('/')[-1]]
        
        # Else return the contents
        return sorted(curr.children.keys())
	
    # Makes a new directory according to the given path
    def mkdir(self, path):
        self.find(path, True)
    
    # Create if filePath does not exist, else update
    def addContentToFile(self, filePath, content):
        curr = self.find(filePath, True)
        curr.content += content

    def readContentFromFile(self, filePath):
        curr = self.find(filePath)
        return curr.content

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)