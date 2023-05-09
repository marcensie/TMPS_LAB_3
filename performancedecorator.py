from models.worker import Worker

class PerformanceReviewDecorator(Worker):
    
    def __init__(self, Worker: Worker, performance_review: str):
        self.Worker = Worker
        self.performance_review = performance_review

    def get_name(self) -> str:
        return self.Worker.get_name()

    def get_salary(self) -> float:
        return self.Worker.get_salary()

    def set_name(self, name: str) -> None:
        self.Worker.set_name(name)

    def set_salary(self, salary: float) -> None:
        self.Worker.set_salary(salary)

    def get_performance_review(self) -> str:
        return self.performance_review

    def get_id(self) -> int:
        return self.Worker.get_id()

    def set_performance_review(self, performance_review: str) -> None:
        self.performance_review = performance_review
