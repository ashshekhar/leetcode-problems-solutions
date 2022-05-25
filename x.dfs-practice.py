visited = []
queue = []
result = []
  
def dfs(visited, graph, node):

  if node not in visited:
    result.append(node)
    visited.append(node)

    for neighbor in graph[node]:
      dfs(visited, graph, neighbor)
  

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
  
  print(dfs(visited, graph, '5'))