visited = []
queue = []
result = []
  
def bfs(visited, graph, node):

  visited.append(node)
  queue.append(node)
  
  while queue:
    print_node = queue.pop()
    result.append(print_node)
    
    for neighbor in graph[print_node]:
      if neighbor not in visited:
        visited.append(neighbor)
        queue.append(neighbor)
  
  return result
    

if __name__ == "__main__":

  graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : [] 
  }
  
  print(bfs(visited, graph, '5'))