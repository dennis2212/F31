import pytest
from exercitiul1 import Employee, Manager

def test_create_employee():
    """Test pentru crearea unui employee"""
    employee = Employee("Employee", 3000)
    assert employee.name == "Employee"
    assert employee.salary == 3000
    assert Employee.empCount == 1
    del employee

def test_manager_creation():
    """Test pentru crearea unui manager"""
    manager = Manager("Manager", 6000, "Architecture")
    assert manager.name == "Manager"
    assert manager.salary == 6000
    assert manager.department == "F31_Architecture"
    assert Manager.mgrCount == 1
    del manager

def test_modify_task():
    """Test pentru adaugarea si afisarea task-urilor unui employee"""
    employee = Employee("Test", 13000)
    employee.modify_task("Task1", "Ended")
    employee.modify_task("Task2", "New")
    assert "Task1" in employee.tasks
    assert employee.tasks["Task1"] == "Ended"
    assert employee.tasks["Task2"] == "New"
    del employee

if __name__ == "__main__":
    pytest.main()