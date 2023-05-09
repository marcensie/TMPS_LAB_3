# TMPS_LAB_3 - Clinic management system
## by Jardan Alexandru

## Objective :
Implement some structural design patterns in a project.

### Facade: The WorkerManagementSystem class serves as a high-level interface that simplifies the usage of the underlying subsystems: Workerdb, PaySystem, and PerformanceReviewSystem.By utilizing the WorkerManagementSystem class, clients can perform common operations on workers without needing to directly interact with the individual subsystems. This simplifies the usage and provides a higher level of abstraction, which is a characteristic of the Facade pattern.
```
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

def main():
    wms = WorkerManagementSystem(db, PaySystem(), review_system)
        Workers = wms.get_Workers()
```



