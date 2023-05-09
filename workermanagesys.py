from workerdb import Workerdb
from paysystem import PaySystem
from performancereview import PerformanceReviewSystem
from models.worker import Worker
from typing import List

class WorkerManagementSystem:
    def __init__(self, Worker_repository: Workerdb, payroll_system: PaySystem, performance_review_system: PerformanceReviewSystem):
        self.Worker_repository = Worker_repository
        self.payroll_system = payroll_system
        self.performance_review_system = performance_review_system

    def get_Workers(self) -> List[Worker]:
        return self.Worker_repository.get_Workers()

    def get_Worker_by_id(self, id: int) -> Worker:
        return self.Worker_repository.get_Worker_by_id(id)

    def add_Worker(self, Worker: Worker) -> None:
        self.Worker_repository.add_Worker(Worker)

    def remove_Worker(self, Worker: Worker) -> None:
        self.Worker_repository.remove_Worker(Worker)

    def pay_Workers(self) -> None:
        self.payroll_system.pay_Workers(self.get_Workers())

    def add_performance_review(self, Worker: Worker, review: str) -> None:
        self.performance_review_system.add_performance_review(Worker, review)

    def get_performance_review(self, Worker: Worker) -> str:
        return self.performance_review_system.get_performance_review(Worker)

    def raise_salary(self, Worker: Worker, amount: float) -> None:
        current_salary = Worker.get_salary()
        Worker.set_salary(current_salary + amount)

