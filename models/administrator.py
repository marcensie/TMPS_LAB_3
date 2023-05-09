from typing import List
from models.worker import Worker

class Administrator(Worker):
    def __init__(self, id: int, name: str, salary: float):
        self.id = id
        self.name = name
        self.salary = salary
        self.subordinates = []

    def add(self, Worker: Worker) -> None:
        self.subordinates.append(Worker)

    def remove(self, Worker: Worker) -> None:
        self.subordinates.remove(Worker)

    def get_subordinates(self) -> List[Worker]:
        return self.subordinates

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
