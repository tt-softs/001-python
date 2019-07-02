"""
Modify your department:
change giving salary method: if there is not Employee in manager's team, raise SalaryGivingError(You should create the Error class)
Add method add_to_team(array) to manager class, which adds employees to team. If there are not Employees in array, raise your own NotEmployeeException and if
Employee is Manager, reise WrongEmployeeRoleError with parameter "second_name". String representation of error should return message "Employee @second_name@
has unexpected role!"
In Department class create method add_team_members(manager, array) which tries to add array of Employees to manager team. Handle the exceptions, raised in
manager's add_to_team method.
"""
from manager import Manager
from developer import Developer
from designer import Designer
from department import Department



def main():

    managers = [
        Manager("Bill", "Gates", 1000, 10),
        Manager("Mark", "Zuckerberg", 900, 3),
        Manager("Sergey", "Brin", 900, 1),
        Manager("Steve", "Jobs", 800, 8)
        ]

    employees = [
        Designer("tom", "taylor", 800, 10, managers[0], effect_coeff=0.5),
        Developer("dev1", "java", 500, 2, managers[0]),
        Developer ("dev2", "js", 500, 6, managers[0]),

        Designer("armani", "jeans", 1200, 3, managers[1], effect_coeff=1),
        Designer("dolce", "gabbana", 800, 6, managers[1]),
        Developer ("dev3", "basic", 500, 0.5, managers[1]),

        Developer ("dev4", "python", 500, 6)
        ]

    depart = Department(managers)

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

    depart.add_team_members(managers[-1], managers[:-1:])
    depart.give_salary()


if __name__ == "__main__":
    main()
