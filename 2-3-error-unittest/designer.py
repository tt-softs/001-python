#import employee
from employee import Employee

class Designer(Employee):
    def __init__(self, first_name, second_name, salary, years_experience, manager = None, effect_coeff=1):
        super().__init__(first_name, second_name, salary, years_experience, manager)
        self.effect_coeff = effect_coeff

    def get_salary(self):
        return int(super().get_salary() * self.effect_coeff)
