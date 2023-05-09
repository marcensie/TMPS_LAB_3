from typing import List
from models.worker import Worker

class Doctor(Worker):
    def __init__(self, id: int, name: str, salary: float):
        self.id = id
        self.name = name
        self.salary = salary

    def add(self, Worker: Worker) -> None:
        pass

    def remove(self, Worker: Worker) -> None:
        pass

    def get_subordinates(self) -> List[Worker]:
        return []

    def get_name(self) -> str:
        return self.name

    def get_salary(self) -> float:
        return self.salary

    def get_id(self) -> int:
        return self.id

    def set_name(self, name: str) -> None:
        self.name = name

    def set_salary(self, salary: float) -> None:
        self.salary = salary
