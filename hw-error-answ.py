"""
Modify your department:
change giving salary method: if there is not Employee in manager's team, raise SalaryGivingError(You should create the Error class)
Add method add_to_team(array) to manager class, which adds employees to team. If there are not Employees in array, raise your own NotEmployeeException and if 
Employee is Manager, reise WrongEmployeeRoleError with parameter "second_name". String representation of error should return message "Employee @second_name@ 
has unexpected role!"
In Department class create method add_team_members(manager, array) which tries to add array of Employees to manager team. Handle the exceptions, raised in 
manager's add_to_team method.
"""

class SalaryGivingError(Exception):
    def __init__(self, message):
        super(SalaryGivingError, self).__init__(message)
        
class NotEmployeeException(Exception):
    def __init__(self, message):
        super(NotEmployeeException, self).__init__(message)
        
class WrongEmployeeRoleError(Exception):
    def __init__(self, message):
        super(WrongEmployeeRoleError, self).__init__("Employee " + message +" has unexpected role!")




class Employee:
    def __init__(self, first_name, second_name, salary, years_experience = 0 , manager = None):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.years_experience = years_experience
        self.manager = None
        self.set_manager(manager)

    def __str__(self):
            return "{} {} {}, experience: {}".format(self.first_name, self.second_name, ", manager "+self.manager.second_name if type(self.manager) == Manager else "", self.years_experience)
            
    def get_salary(self):
        if self.years_experience > 5:
            return int(self.salary * 1.2 + 500)
        if self.years_experience > 2:
            return int(self.salary + 200)
        return self.salary
        
    def set_manager(self, manager = None):
        manager = manager if type(manager) == Manager else None
        if self.manager == manager :
            return
        if self.manager != None:
            self.manager.team.remove(self)
        self.manager = manager
        if manager != None:
            manager.team.append(self)
        
class Developer(Employee):
    def __init__(self, first_name, second_name, salary, years_experience, manager = None):
        super().__init__(first_name, second_name, salary, years_experience, manager)


class Designer(Employee):
    def __init__(self, first_name, second_name, salary, years_experience, manager = None, effect_coeff=1):
        super().__init__(first_name, second_name, salary, years_experience, manager)
        self.effect_coeff = effect_coeff

    def get_salary(self):
        return int(super().get_salary() * self.effect_coeff)


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
            return int(koef * (super().get_salary() + 300))
        if len(self.team) > 5:
            return int(koef * (super().get_salary() + 200))
        return int(koef * (super().get_salary()))

    def add_to_team(self, array):
        if( not isinstance(array, list)  or sum( isinstance(i,Employee) for i in array) == 0 ): #len(array) == None
            raise NotEmployeeException("NotEmployeeException: " + str(array))
        for candidate in array:
            try:
                if type(candidate) is  Manager: # not in (Designer, Developer) #
                    raise WrongEmployeeRoleError(candidate.second_name)
                if isinstance(candidate, Designer) or isinstance(candidate, Developer):
                    candidate.set_manager(self)
            except WrongEmployeeRoleError as e:
                print(e)                    


class Department:
    def __init__(self, managers=None):
        self._managers = [] if managers is None  else managers

    def append_to_department(self, manager):
        if manager not in self._managers:
            self._managers.append(manager)
          
    def give_salary(self):
        for i, manager in enumerate(self._managers, 1):
            print("{}) Manager: {} got BIG salary:{}".format(i, manager, manager.get_salary()))
            try:
                if not manager.get_team(): # if len(manager.get_team()) == 0 :
                    raise SalaryGivingError( " SalaryGivingError: ({}) not have team!".format( str(manager) ) )
                for j, employee in enumerate( manager.get_team(), 1 ):
                    print("{}.{}) Employee: {} had salary:{}".format(i, j, employee, employee.get_salary()))
            except SalaryGivingError as e:
                print( e ) #e.args[0] )
        print("****************End of Department's Salary ************************")
        
    def add_team_members(self, manager, array):
        try:
            manager.add_to_team(array)
        except NotEmployeeException as e:
            print(e)
        except WrongEmployeeRoleError as e:
            print(e)  

def main():

    managers = [ 
        Manager("Bill", "Gates", 1000, 10),  
        Manager("Mark", "Zuckerberg", 900, 3), 
        Manager("Sergey", "Brin", 900, 1), 
        Manager("Steve", "Jobs", 800, 8) 
        ]
    depart = Department(managers)
    
    employees = [ 
        Designer("tom", "taylor", 800, 10, managers[0], effect_coeff=0.5), 
        Developer("dev1", "java", 500, 2, managers[0]),
        Developer ("dev2", "js", 500, 6, managers[0]),
        
        Designer("armani", "jeans", 1200, 3, managers[1], effect_coeff=1), 
        Designer("dolce", "gabbana", 800, 6, managers[1]),
        Developer ("dev3", "basic", 500, 0.5, managers[1]),
        
        Developer ("dev4", "python", 500, 6)
        ]
        
    wrong_list = ["vasya","petya","kolya", 15, True]
    
    depart.give_salary()
    
    depart.add_team_members(managers[-1], employees[-1::]) # employees[-1].set_manager(managers[-1])
    depart.give_salary()
    
    depart.add_team_members(managers[-2], employees[-1::])  #employees[-1].set_manager(managers[-2])
    depart.give_salary()
    
    depart.add_team_members(managers[1], employees[-1::]) # employees[-1].set_manager()
    depart.give_salary()

    depart.add_team_members(managers[0], employees) 
    depart.give_salary()
    
    depart.add_team_members(managers[-1], [])
    depart.give_salary()

    depart.add_team_members(managers[-1], wrong_list)
    depart.give_salary() 

    wrong_list.extend(employees[-1::])
    depart.add_team_members(managers[-1], wrong_list)
    depart.give_salary() 
    
    depart.add_team_members(managers[-2], managers[-1::]) 
    depart.give_salary()
    
    depart.add_team_members(managers[0], managers[1::]) 
    depart.give_salary()
    
if __name__ == "__main__":
    main()

