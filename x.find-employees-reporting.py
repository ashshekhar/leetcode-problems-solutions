# Recursive DP function to find all employees who directly or indirectly
# report to a given manager and store the result in `result`
def findReportings(employee_to_manager_mapping):

  # Helper
  mixed_manager_to_employee_mapping  = {}
  
  # To return
  manager_to_employee_mapping = {}
  
  # Reverse the input to run DFS on it
  for employee, manager in employee_to_manager_mapping.items():

      if employee == manager:
        continue
      
      if manager not in mixed_manager_to_employee_mapping:
          mixed_manager_to_employee_mapping[manager] = set()
          
      mixed_manager_to_employee_mapping[manager].add(employee)

  # Add the empty list managers who are employees
  for employees in employee_to_manager_mapping.keys():
      if employees not in mixed_manager_to_employee_mapping:
        mixed_manager_to_employee_mapping[employees] = set()
  
  
  # Using DFS to update the result dictionary
  def dfs(manager):
    
    # Base Case
    if manager in manager_to_employee_mapping:
      return manager_to_employee_mapping[manager]

    # List of employees of current manager node
    employees_of_manager = mixed_manager_to_employee_mapping[manager]
    
    # For each of those employees, recursively find a list of all of their employees
    for employees in employees_of_manager.copy():
      
      list_of_employees_reporting_to_employees = dfs(employees)
      
      # Update the list previously generated if there are new values
      if list_of_employees_reporting_to_employees:
        employees_of_manager.update(list_of_employees_reporting_to_employees)
    
    # Update the final return dictionary and return
    manager_to_employee_mapping[manager] = employees_of_manager
    
    return employees_of_manager
  
  # Calling DFS after creating the necessary mappings
  for manager in mixed_manager_to_employee_mapping.keys():
    dfs(manager)
  
  return manager_to_employee_mapping

if __name__ == '__main__':
  
    employee_to_manager_mapping = {'A': 'A', 'B': 'A', 'C': 'B', 'D': 'B', 'E': 'D', 'F': 'E'}
    
    result = findReportings(employee_to_manager_mapping)
    
    print(result)