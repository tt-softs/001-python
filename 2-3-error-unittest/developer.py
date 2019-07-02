from employee import Employee

class Developer(Employee):
    def __init__(self, first_name, second_name, salary, years_experience, manager = None):
        super().__init__(first_name, second_name, salary, years_experience, manager)
