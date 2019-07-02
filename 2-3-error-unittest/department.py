from excepts import SalaryGivingError, NotEmployeeException, WrongEmployeeRoleError

class Department:
    def __init__(self, managers=None):
        self._managers = [] if managers is None  else managers

    def append_to_department(self, manager):
        if manager not in self._managers:
            self._managers.append(manager)

    def give_salary(self):
        for i, manager in enumerate(self._managers, 1):
            try:
                print("{}) Manager: {} got BIG salary:{}".format(i, manager, manager.get_salary()))
                for j, employee in enumerate( manager.get_team(), 1 ):
                    print("{}.{}) Employee: {} had salary:{}".format(i, j, employee, employee.get_salary()))
            except SalaryGivingError as e:
                print( e )
        print("****************End of Department's Salary ************************\n")

    def add_team_members(self, manager, array):
        try:
            manager.add_to_team(array)
        except NotEmployeeException as e:
            print(e)
        except WrongEmployeeRoleError as e:
            print(e)
