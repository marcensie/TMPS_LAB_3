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

### Composite: The Administrator class represents a composite object that can have subordinates of the same type (Worker). The Administrator class extends the Worker class, indicating that it is part of the worker hierarchy. By organizing workers (including administrators) in a tree-like structure, where administrators can have subordinates, the Composite pattern allows treating individual workers and groups of workers uniformly.
```
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
```

### Decorator: The PerformanceReviewDecorator class decorates a Worker object by adding additional behavior related to performance reviews. The PerformanceReviewDecorator class extends the Worker class, indicating that it conforms to the same interface as a Worker object. It wraps an existing Worker object and adds functionality specific to performance reviews.
```
Class PerformanceReviewDecorator(Worker):
    
    def __init__(self, Worker: Worker, performance_review: str):
        self.Worker = Worker
        self.performance_review = performance_review

    def get_name(self) -> str:
        return self.Worker.get_name()

    def get_performance_review(self) -> str:
        return self.performance_review

    def get_id(self) -> int:
        return self.Worker.get_id()

    def set_performance_review(self, performance_review: str) -> None:
        self.performance_review = performance_review

```

### Flyweight: The SectionCache class serves as a cache to store and reuse Section objects based on their name. The SectionCache class maintains a dictionary (Sections) that acts as a storage for Section objects. The keys of the dictionary represent the unique identifiers (names) for each section. The get_Section method takes a name and description as parameters. It first checks if a Section object with the given name already exists in the cache. If it does, the existing Section object is returned. By reusing existing Section objects instead of creating new ones, the Flyweight pattern reduces memory consumption, especially when multiple sections with the same name are required.
```
class Section:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class SectionCache:
    Sections: Dict[str, Section] = {}

    def get_Section(name: str, description: str) -> Section:
        Section = SectionCache.Sections.get(name)

        if Section is None:
            Section = Section(name, description)
            SectionCache.Sections[name] = Section

        return Section

```




