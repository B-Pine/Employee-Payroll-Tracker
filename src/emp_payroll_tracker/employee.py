from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(
        self,
        employee_id: str,
        name: str,
        salary: float,
        bonus: float = 0,
        tax: float = 0,
    ):
       self.employee_id = employee_id
       self.name = name
       self._salary = salary
       self.bonus = bonus
       self.tax = tax

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if self._salary <= 0:
            print("Invalid value for salary")
        else:
            
    
    @abstractmethod
    def calculate_salary(self) -> float:
        ...