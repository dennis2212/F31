class Employee:
    """Common base class for all employees."""
    empCount = 0 #Variabila pentru a numara employees.

    def __init__(self, name, salary):
        """Un constructor, initializeaza un Employee cu un nume, salariu si un dictionary de task-uri."""
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        """Afiseaza numarul total de employees."""
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        """Afiseaza informatiile despre un employee(nume si salariu)."""
        print("Name: ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        """Decrementeaza numarul de employees atunci cand un obiect se sterge."""
        Employee.empCount -= 1

    def update_salary(self, new_salary):
        """Modifica salariul unui employee cu o valoare data."""
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        """Modifica(sau adauga in dictionar) task-ul unui employee cu un status(initial status "New")."""
        self.tasks[task_name] = status

    def display_task(self, status):
        """Afiseaza fiecare task al unui employee cu un status dat."""
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgrCount = 0 #Variabila pentru a numara managers.

    def __init__(self, name, salary, department):
        """Un constructor, initializeaza un Manager si cu informatii suplimentare despre departament."""
        super().__init__(name, salary)
        self.department = f"F31_{department}"
        Manager.mgrCount += 1

    def display_employee(self):
        """Afiseaza informatiile despre un manager dupa cerinta ceruta(X%3==1)."""
        print(f"Salary: {self.salary}")

    def __del__(self):
        """Decrementeaza numarul de managers atunci cand un obiect se sterge, cat si numarul de employees."""
        super().__del__()
        Manager.mgrCount -= 1

if __name__ == "__main__":
    #Crearea obiectelor Manager(Y/3=4-aproximativ) si punerea lor intr-o lista.
    managers = []
    manager1 = Manager("Kevin", 4000, "Cybersecurity")
    managers.append(manager1)
    manager2 = Manager("Denis", 4500, "Marketing")
    managers.append(manager2)
    manager3 = Manager("Bianca", 3500, "HR")
    managers.append(manager3)
    manager4 = Manager("Ana", 4000, "Development")
    managers.append(manager4)

    #Afisarea informatiilor pentru manageri, necesare cerintei.
    for mgr in managers:
        mgr.display_employee()

    #Crearea unui obiect Employee si afisarea informatiilor sale pentru claritate.
    employee = Employee("Employee", 3000)
    employee.display_employee()

    #Afisarea numarului total de employees si managers.
    print(f"Numarul de employees este: {Employee.empCount}")
    print(f"Numarul de managers este: {Manager.mgrCount}")
