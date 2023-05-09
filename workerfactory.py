from models.doctor import Doctor
from models.administrator import Administrator
from models.worker import Worker

class WorkerFactory:
    def create_Worker(self, type: str, id: int, name: str, salary: float) -> Worker:
        type = type.lower()
        if type == "doctor":
            return Doctor(id, name, salary)
        elif type == "administrator":
            return Administrator(id, name, salary)
        else:
            raise ValueError("Invalid Worker type: " + type)
