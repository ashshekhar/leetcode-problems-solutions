def QuickSort(arr):
  
    elements = len(arr)
    
    #Base case
    if elements < 2:
        return arr
    
    # Position of the partitioning element
    current_position = 0 

    # Partitioning loop
    for i in range(1, elements): 
      
        # Found a lesser number than partitioning element
        # Increment the frontier or parititon and add in the encountered smaller number
        # There can be some larger numbers in between the frontier and the encountered smaller number
        # Therefore, use swapping
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    # Brings pivot to it's appropriate position
    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp 
    
    # Divide and Conquer
    left = QuickSort(arr[0:current_position]) # Sorts the elements to the left of pivot
    right = QuickSort(arr[current_position+1:elements]) # Sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right # Merging everything together
    
    return arr