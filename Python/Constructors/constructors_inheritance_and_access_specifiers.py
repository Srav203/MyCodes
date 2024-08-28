# Base class for Employee
class Employee:
    # Public data member
    name = None
    
    # Protected data member
    _id = None
    
    # Private data member
    __salary = None

    # Constructor
    def __init__(self, name, emp_id, salary):
        self.name = name
        self._id = emp_id
        self.__salary = salary
    
    def displayName(self):
        print("Employee Name:", self.name)
    
    def _displayID(self):
        print("Employee ID:", self._id)
    
    def __displaySalary(self):
        print("Salary:", self.__salary)
    
    def accessSalary(self):
        self.__displaySalary()

# Derived class for Manager
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department
    
    def accessID(self):
        self._displayID()

    def displayDepartment(self):
        print("Department:", self.department)

# Derived class for Intern
class Intern(Employee):
    def __init__(self, name, emp_id, salary, mentor):
        super().__init__(name, emp_id, salary)
        self.mentor = mentor
    
    def displayMentor(self):
        print("Mentor:", self.mentor)

# Creating objects of derived classes
manager = Manager("Alice", 101, 75000, "HR")
intern = Intern("Bob", 102, 15000, "Alice")

# Calling public methods
manager.displayName()
manager.accessID()
manager.accessSalary()
manager.displayDepartment()

intern.displayName()
intern.displayMentor()
intern.accessSalary()

# Accessing protected member directly (valid)
print("Accessing protected member directly:", manager._id)

# Attempt to access private member directly (will cause an error if uncommented)
# print(intern.__salary)
