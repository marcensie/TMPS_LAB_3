from models.administrator import Administrator

class AdministratorBuilder:
    def __init__(self):
        self.name = None
        self.salary = None
        self.id = None

    def set_name(self, name: str) -> 'AdministratorBuilder':
        self.name = name
        return self

    def set_salary(self, salary: float) -> 'AdministratorBuilder':
        self.salary = salary
        return self

    def set_id(self, id: int) -> 'AdministratorBuilder':
        self.id = id
        return self

    def build(self) -> Administrator:
        return Administrator(self.id, self.name, self.salary)
