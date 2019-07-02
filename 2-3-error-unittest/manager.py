from employee import Employee
from developer import Developer
from designer import Designer
from excepts import SalaryGivingError, NotEmployeeException, WrongEmployeeRoleError

class Manager(Employee):
    def __init__(self, first_name, second_name, salary, years_experience, manager = None, team = None):
        super().__init__(first_name, second_name, salary, years_experience, manager)
        self.team = [] if team is None  else team

    def get_team(self):
        return self.team

    def get_salary(self):
        koef = 1.1  if ( sum(type(i) == Developer for i in self.team) > len(self.team) / 2 ) else 1
        #koef = 1.1  if len(filter(lambda i: type(i) is Developer , self.team)) > len(self.team) / 2 else 1
        if len(self.team) > 10:
            total_salary = int(koef * (super().get_salary() + 300))
        elif len(self.team) > 5:
            total_salary = int(koef * (super().get_salary() + 200))
        else:
            total_salary = int(koef * (super().get_salary()))
        if not self.get_team(): # if len(manager.get_team()) == 0 :
            raise SalaryGivingError( " SalaryGivingError: ({}) not have team, but got salary: {} !".format( str(self), str(total_salary) ) )
        return total_salary

    def add_to_team(self, array):
        if( not isinstance(array, list)  or sum( isinstance(i,Employee) for i in array) == 0 ): #len(array) == None
            raise NotEmployeeException("NotEmployeeException: " + str(array))
        candidate_manager = None
        for candidate in array:
            if type(candidate) is  Manager:
                candidate_manager = candidate
            elif isinstance(candidate, Designer) or isinstance(candidate, Developer):
                candidate.set_manager(self)
        if isinstance(candidate_manager, Manager):
            raise WrongEmployeeRoleError(candidate_manager.second_name)
