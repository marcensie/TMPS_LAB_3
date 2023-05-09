from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_salary(self) -> float:
        pass

    @abstractmethod
    def get_id(self) -> int:
        pass

    @abstractmethod
    def set_name(self, name: str) -> None:
        pass

    @abstractmethod
    def set_salary(self, salary: float) -> None:
        pass
