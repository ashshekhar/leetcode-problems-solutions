def minimum_energy(checkpoints):
  minimum_energy = 1
  total_energy = 0

  for checkpoint in checkpoints:
  
    total_energy += checkpoint

    if(total_energy < 0):
      minimum_energy = total_energy 
      
      1 - checkpoint
    
  return minimum_energy



def main():
  example = [-1,-5,-9]
  print(minimum_energy(example))

main()