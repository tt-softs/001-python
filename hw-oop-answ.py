"""Create structure for department:
There are 3 types of employee: developer, designer and manager
Each employee has: first name, second name, salary, experiance (years)
Each designer, developer or manager can have higher managers
Each designer has effectivness coefficient(0-1)
Each manager has team of developers and designers.
Department should have list of managers(which have their own teams)
Department should be able to give salary (for each employee message: "@firstName@ @secondName@: got salary: @salaryValue@")
Each employee gets the salary, defined in field Salary. If experiance of employee is > 2 years, he gets bonus + 200$, if experiance is > 5 years, he gets salary*1.2 + bonus 500
Each designer gets the salary = salary*effCoeff
Each manager gets salary +
200$ if his team has >5 members
300$ if his team has >10 members
salary*1.1 if more than half of team members are developers.
Redefine string representation for employee as follows: "@firstName@ @secondName@, manager:@manager secondName@, experiance:@experiance@"
"""


class Employee:
    def __init__(self, first_name, second_name, salary, years_experience = 0 , manager = None):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.years_experience = years_experience
        self.manager = None
        self.set_manager(manager)

    def __str__(self):
            return "{} {}, manager: {}, experience: {}".format(self.first_name, self.second_name, self.manager.second_name if type(self.manager) == Manager else self.manager, self.years_experience)
            
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


class Department:
    def __init__(self, managers=None):
        self._managers = [] if managers is None  else managers

    def append_to_department(self, manager):
        if manager not in self._managers:
            self._managers.append(manager)
          
    def give_salary(self):
        for i in range(0, len(self._managers)):
            print("{}) Manager: {} had salary:{}".format(i+1, self._managers[i], self._managers[i].get_salary()))
            for j in range(0, len(self._managers[i].get_team())):
                employee = self._managers[i].team[j]
                print("{}.{}) Employee: {} had salary:{}".format(i+1, j+1, employee, employee.get_salary()))
        print("****************End of Department's Salary ************************")


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
        
    depart.give_salary()
    
    employees[-1].set_manager(managers[-1])
    depart.give_salary()
    
    employees[-1].set_manager(managers[-2])
    depart.give_salary()
    
    employees[-1].set_manager()
    depart.give_salary()
    
if __name__ == "__main__":
    main()

