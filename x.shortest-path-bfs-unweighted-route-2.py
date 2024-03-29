# Class representing node of a graph
class Node:
  def __init__(self, name):
    self.name = name
    self.prev = None
    self.neighbors = []
    self.visited = False

  # Method to connect nodes
  def add_neighbor(self, node):
    self.neighbors.append(node)
    node.neighbors.append(self)

  # Node representaion
  def __repr__(self):
    return self.name

class ShortestPath:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def BFS(self):
    # Create queue
    queue = []
    
    # Visit and add the start node to the queue
    self.start.visited = True
    queue.append(self.start)

    # BFS until queue is empty
    while queue:
      # Pop a node from queue for search operation
      current_node = queue.pop(0)
      
      # Loop through neighbors nodes to find the 'end' node
      for node in current_node.neighbors:
        if not node.visited:
          
          # Visit and add neighbors nodes to the queue
          node.visited = True
          queue.append(node)
          
          # Update its preceding node
          node.prev = current_node
          
          # Stop BFS if the visited node is the end node 
          if node == self.end:
            queue.clear()
            break;
          
    # BFS completed, now trace the route    
    self.trace_route()

  # Function to trace the route using preceding nodes
  def trace_route(self):
    node = self.end
    route = []
    
    # Start node has no preceding node so loop until node->prev is null 
    while node:
      route.append(node)
      node = node.prev
      
    # Reverse the route bring start to the front
    route.reverse()
    
    # Output route
    print(route)
    
if __name__ == '__main__':
  #create nodes
  node_A = Node('A')
  node_B = Node('B')
  node_C = Node('C')
  node_D = Node('D')
  node_E = Node('E')
  
  #connect nodes (i.e. create graph)
  node_A.add_neighbor(node_B)
  node_B.add_neighbor(node_C)
  node_C.add_neighbor(node_D)
  node_D.add_neighbor(node_E)
  node_B.add_neighbor(node_E)
  
  # Given graph
  # A - B - C - D
  #     \      /
  #        E
  
  ShortestPath(node_A, node_E).BFS()
  # Answer should be A B E