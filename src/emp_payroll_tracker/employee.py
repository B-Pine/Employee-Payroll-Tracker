from abc import ABC, abstractmethod


class Employee(ABC):
    """Base class for all employee types."""

    def __init__(
        self,
        employee_id: str,
        name: str,
        salary: float,
        bonus: float = 0.0,
        tax: float = 0.0,
    ) -> None:
        
        employee_id = employee_id.strip()
        name = name.strip()

        if not employee_id:
            raise ValueError("Employee ID cannot be empty.")

        if not name:
            raise ValueError("Employee name cannot be empty.")

        self.employee_id = employee_id
        self.name = name

        self.salary = salary
        self.bonus = bonus
        self.tax = tax

    @property
    def salary(self) -> float:
        """Return the employee's base salary."""
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        """Validate and update salary."""
        if value <= 0:
            raise ValueError("Salary must be greater than 0.")

        self._salary = float(value)

    @property
    def bonus(self) -> float:
        """Return the employee's bonus."""
        return self._bonus

    @bonus.setter
    def bonus(self, value: float) -> None:
        """Validate and update bonus."""
        if value < 0:
            raise ValueError("Bonus cannot be negative.")

        self._bonus = float(value)

    @property
    def tax(self) -> float:
        """Return tax rate as a decimal such as 0.10 for 10%."""
        return self._tax

    @tax.setter
    def tax(self, value: float) -> None:
        """Validate and update tax rate."""
        if not 0 <= value <= 1:
            raise ValueError("Tax must be between 0 and 1.")

        self._tax = float(value)

    @abstractmethod
    def calculate_salary(self) -> float:
        """Calculate gross salary for this employee."""
        raise NotImplementedError

    def __str__(self) -> str:
        
        return (
            f"{self.employee_id} - "
            f"{self.name} "
            f"({self.__class__.__name__})"
        )

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (
            f"{self.__class__.__name__}("
            f"employee_id={self.employee_id!r}, "
            f"name={self.name!r}, "
            f"salary={self.salary}, "
            f"bonus={self.bonus}, "
            f"tax={self.tax})"
        )


class FullTimeEmployee(Employee):
    """Employee paid a fixed salary plus a bonus."""

    def calculate_salary(self) -> float:
        return self.salary + self.bonus


class ContractEmployee(Employee):
    """Employee paid according to contract days worked."""

    def __init__(
        self,
        employee_id: str,
        name: str,
        salary: float,
        contract_days: int,
        days_worked: int,
        bonus: float = 0.0,
        tax: float = 0.0,
    ) -> None:
        super().__init__(
            employee_id,
            name,
            salary,
            bonus,
            tax,
        )

        if contract_days <= 0:
            raise ValueError(
                "Contract days must be greater than 0."
            )

        if not 0 <= days_worked <= contract_days:
            raise ValueError(
                "Days worked must be between 0 "
                "and the total contract days."
            )

        self.contract_days = contract_days
        self.days_worked = days_worked

    def calculate_salary(self) -> float:
        daily_rate = self.salary / self.contract_days

        return (
            daily_rate * self.days_worked
        ) + self.bonus


class Intern(Employee):
    """Intern paid a stipend, bonus, and transport allowance."""

    def __init__(
        self,
        employee_id: str,
        name: str,
        salary: float,
        transport_allowance: float = 0.0,
        bonus: float = 0.0,
        tax: float = 0.0,
    ) -> None:
        super().__init__(
            employee_id,
            name,
            salary,
            bonus,
            tax,
        )

        if transport_allowance < 0:
            raise ValueError(
                "Transport allowance cannot be negative."
            )

        self.transport_allowance = float(
            transport_allowance
        )

    def calculate_salary(self) -> float:
        return (
            self.salary
            + self.bonus
            + self.transport_allowance
        )
    