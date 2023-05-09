from models.worker import Worker

class Workerdb:
    def __init__(self):
        self.Workers = []

    def get_Workers(self) -> list[Worker]:
        return self.Workers

    def get_Worker_by_id(self, id: int) -> Worker:
        for Worker in self.Workers:
            if Worker.get_id() == id:
                return Worker
        return None

    def add_Worker(self, Worker: Worker) -> None:
        self.Workers.append(Worker)

    def remove_Worker(self, Worker: Worker) -> None:
        self.Workers.remove(Worker)
