from models.worker import Worker

class PerformanceReviewSystem:
    def __init__(self):
        self.performance_reviews = {}

    def add_performance_review(self, Worker: Worker, review: str) -> None:
        self.performance_reviews[Worker] = review

    def get_performance_review(self, Worker: Worker) -> str:
        return self.performance_reviews.get(Worker)
