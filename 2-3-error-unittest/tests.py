"""
Cover your basics task functions with unit tests. (Possible to use setUp() while testing)
"""
import unittest

from manager import Manager
from developer import Developer
from designer import Designer
from department import Department
from excepts import SalaryGivingError, NotEmployeeException, WrongEmployeeRoleError

class TestEmployeeMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setup Class working")

    @classmethod
    def tearDownClass(cls):
        print("tearDown Class  ending")

    def setUp(self):
        self.managers = [
            Manager("Bill", "Gates", 1000, 10),
            Manager("Mark", "Zuckerberg", 900, 3),
            Manager("Sergey", "Brin", 900, 1),
            Manager("Steve", "Jobs", 800, 8)
            ]
        self.depart = Department(self.managers)

        self.employees = [
            Designer("tom", "taylor", 800, 10, self.managers[0], effect_coeff=0.5),
            Developer("dev1", "java", 500, 2, self.managers[0]),
            Developer ("dev2", "js", 500, 6, self.managers[0]),

            Designer("armani", "jeans", 1200, 3, self.managers[1], effect_coeff=1),
            Designer("dolce", "gabbana", 800, 6, self.managers[1]),
            Developer ("dev3", "basic", 500, 0.5, self.managers[1]),

            Developer ("dev4", "python", 500, 6)
            ]
        self.employees_salary_expected = [730 , 500, 1100]
        self.managers_salary_expected = [1870]
        self.wrong_list = ["vasya","petya","kolya", 15, True]


    def test_get_salary_designer(self):
        self.assertEqual(self.employees[0].get_salary(), self.employees_salary_expected[0])

    def test_get_salary_dev1(self):
        self.assertEqual(self.employees[1].get_salary(), self.employees_salary_expected[1])

    def test_get_salary_dev2(self):
        self.assertEqual(self.employees[2].get_salary(), self.employees_salary_expected[2])

    def test_get_salary_manager(self):
        self.assertEqual(self.managers[0].get_salary(), self.managers_salary_expected[0])

    def test_exception_no_employee_blank_list(self):
        self.assertRaises(NotEmployeeException, self.managers[-1].add_to_team, [])

    def test_exception_no_employee_wrong_list(self):
        self.assertRaises(NotEmployeeException, self.managers[-1].add_to_team, self.wrong_list)

    def test_exception_no_employee_simple_value(self):
        self.assertRaises(NotEmployeeException, self.managers[-1].add_to_team, self.wrong_list[0])

    def test_exception_wrong_employee_role_big_list(self):
        self.assertRaises(WrongEmployeeRoleError, self.managers[0].add_to_team, self.managers[1::])

    def test_exception_wrong_employee_role_simple_list(self):
        self.assertRaises(WrongEmployeeRoleError, self.managers[-2].add_to_team, self.managers[-1::])

    def test_exception_salary_giving_error_empty_team(self):
        self.assertRaises(SalaryGivingError, self.managers[-1].get_salary)

    def test_exception_salary_giving_error_empty_team_once_more(self):
        self.assertRaises(SalaryGivingError, self.managers[-2].get_salary)


if __name__ == '__main__':
    unittest.main()
# suite = unittest.TestLoader().loadTestsFromTestCase(TestEmployeeMethods)
# unittest.TextTestRunner(verbosity=2).run(suite)
