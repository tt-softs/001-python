import manager as mgr

class Employee:
    def __init__(self, first_name, second_name, salary, years_experience = 0 , manager = None):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.years_experience = years_experience
        self.manager = None
        self.set_manager(manager)

    def __str__(self):
            return "{} {} {}, experience: {}".format(self.first_name, self.second_name, ", manager "+self.manager.second_name if type(self.manager) == mgr.Manager else "", self.years_experience)

    def get_salary(self):
        if self.years_experience > 5:
            return int(self.salary * 1.2 + 500)
        if self.years_experience > 2:
            return int(self.salary + 200)
        return self.salary

    def set_manager(self, manager = None):
        manager = manager if type(manager) == mgr.Manager else None
        if self.manager == manager :
            return
        if self.manager != None:
            self.manager.get_team().remove(self)
        self.manager = manager
        if manager != None:
            manager.get_team().append(self)
