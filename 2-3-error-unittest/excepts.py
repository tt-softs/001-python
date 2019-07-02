
class SalaryGivingError(Exception):
    def __init__(self, message):
        super(SalaryGivingError, self).__init__(message)

class NotEmployeeException(Exception):
    def __init__(self, message):
        super(NotEmployeeException, self).__init__(message)

class WrongEmployeeRoleError(Exception):
    def __init__(self, message):
        super(WrongEmployeeRoleError, self).__init__("Employee " + message +" has unexpected role!")
