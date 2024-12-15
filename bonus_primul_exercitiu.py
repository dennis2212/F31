import pytest
from primul_exercitiu import Employee, Manager


def test_create_employee():
    emp = Employee("Test Angajat", 4200)
    assert emp.name == "Test Angajat"
    assert emp.salary == 4200
    assert Employee.empCount == 1
    del emp 

def test_update_salary():
    emp = Employee("Test Angajat", 3000)
    emp.update_salary(4500)          
    assert emp.salary == 4500       
    del emp

def test_create_manager():
    mgr = Manager("Test Manager", 4800, "Tech")
    assert mgr.departament == "F31-Tech"
    assert Manager.mgr_count == 1
    del mgr  

if __name__ == "__main__":
    test_create_employee()
    test_update_salary()
    test_create_manager()
    print("Toate testele merg!")