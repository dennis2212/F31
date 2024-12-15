class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)
    def __del__(self):
        Employee.empCount -= 1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, departament):
        NUME_ECHIPA = "F31-"
        super().__init__(name, salary) 
        self.departament = NUME_ECHIPA + departament
        Manager.mgr_count += 1

    def display_employee(self):
        print(f"Departament: {self.departament}")

    def __del__(self):
        Manager.mgr_count -= 1
    
if __name__ == "__main__":

    manager1 = Manager("Andrei", 3800, "Tester")
    manager2 = Manager("Mihai", 3200, "Software")
    manager3 = Manager("Oana", 2200, "Marketing")
    manager4 = Manager("Alin", 3500, "Networking")

    manager1.display_employee()
    manager2.display_employee()
    manager3.display_employee()
    manager4.display_employee()

    print(f"Numărul de manageri este: {Manager.mgr_count}")
    print(f"Numărul total de angajați este: {Employee.empCount}")