#
# @lc app=leetcode id=1376 lang=python
#
# [1376] Time Needed to Inform All Employees
#

# @lc code=start
class Solution(object):

    def dfs(self, res, time, node, visited, manager_to_subordinate):
        
        # Base case: Only inform time stores
        if not len(manager_to_subordinate):
            return 0

        # Base case
        if len(manager_to_subordinate[node]) == 1:
            return time

        time += manager_to_subordinate[node][0]

        for subordinates in manager_to_subordinate[node][1:]:
            if subordinates not in visited:
                visited.add(subordinates)
                
                # For each stage, you need to store the max ever encountered
                res = max(res, self.dfs(res, time, subordinates, visited, manager_to_subordinate))
        
        return res

    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        # Key is n value of the employee, value is (time to infrom, [list of subordinates])
        # Use of backtracking - Similar to course schedule
        manager_to_subordinate = {}
        
        # time = 0
        visited = set()
        
        # Creating dictionary mapping
        for subordinate, manager in enumerate(manager):
            if manager == -1:
                continue
                
            if manager not in manager_to_subordinate:
                manager_to_subordinate[manager] = [informTime[manager]]
                
            manager_to_subordinate[manager].append(subordinate)
            
            # For the rest of the subordinates
            if subordinate not in manager_to_subordinate:
                manager_to_subordinate[subordinate] = [informTime[subordinate]]
                
        res = self.dfs(0, 0, headID, visited, manager_to_subordinate)
            
        return res 
# @lc code=end



def findAllReportingEmployees(manager, managerToEmployeeMappings, result):
   
    # if the subproblem is already seen before
    if manager in result:
        # return the already computed mapping
        return result.get(manager)
 
    # find all employees reporting directly to the current manager
    managerEmployees = managerToEmployeeMappings.get(manager)
 
    # find all employees reporting indirectly to the current manager
    for reportee in managerEmployees.copy():
        # find all employees reporting to the current employee
        employees = findAllReportingEmployees(reportee, managerToEmployeeMappings,
                                                result)
 
        # move those employees to the current manager
        if employees:
            managerEmployees.update(employees)
 
    # save the result to avoid recomputation and return it
    result[manager] = managerEmployees
    return managerEmployees
 
 
# Find all employees who directly or indirectly reports to a manager
def findEmployees(employeeToManagerMappings):
 
    # store manager to employee mappings in a new dictionary
    managerToEmployeeMappings = {}
 
    # fill the above dictionary with the manager to employee mappings
    for employee, manager in employeeToManagerMappings.items():
        managerToEmployeeMappings.setdefault(employee, set())
        # don't map an employee with itself
        if employee != manager:
            managerToEmployeeMappings.setdefault(manager, set()).add(employee)
 
    # construct an empty dictionary to store the result
    result = {}
 
    # find all reporting employees (direct and indirect) for every manager
    # and store the result in a dictionary
    for key in employeeToManagerMappings.keys():
        findAllReportingEmployees(key, managerToEmployeeMappings, result)
 
    return result
 
 
if __name__ == '__main__':
 
    # construct a mapping from employee to manager
    employeeToManagerMappings = {'A': 'A', 'B': 'A', 'C': 'B',
                                'D': 'B', 'E': 'D', 'F': 'E'}
    result = findEmployees(employeeToManagerMappings)
 
    # print contents of the resulting dictionary
    for key, value in result.items():
        print(key, '—>', value)
 
