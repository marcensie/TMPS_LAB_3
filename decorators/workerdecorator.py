from models.worker import Worker

class WorkerDecorator(Worker):

    def set_performance_review(self, performance_review: str) -> None:
        pass

    def get_performance_review(self) -> str:
        pass
