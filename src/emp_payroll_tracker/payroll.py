from .employee import Employee


def calculate_salary(employee: Employee) -> float:
    """Calculate gross salary for an employee."""
    return employee.calculate_salary()


def apply_tax(
    gross_salary: float,
    tax: float,
) -> float:
    """Calculate tax deducted from gross salary."""

    if gross_salary < 0:
        raise ValueError(
            "Gross salary cannot be negative."
        )

    if not 0 <= tax <= 1:
        raise ValueError(
            "Tax must be between 0 and 1."
        )

    return gross_salary * tax


def generate_payslip(
    employee: Employee,
) -> dict[str, object]:
    """Generate one employee's payroll information."""

    gross_salary = calculate_salary(employee)

    tax_amount = apply_tax(
        gross_salary,
        employee.tax,
    )

    net_salary = gross_salary - tax_amount

    return {
        "employee_id": employee.employee_id,
        "name": employee.name,
        "role": employee.__class__.__name__,
        "gross_salary": gross_salary,
        "tax_rate": employee.tax,
        "tax_amount": tax_amount,
        "net_salary": net_salary,
    }


def process_payroll(
    employees: list[Employee],
) -> dict[str, dict[str, object]]:
    """Generate payroll records for all employees."""

    return {
        employee.employee_id: generate_payslip(employee)    # generating employees payslip using dictionary comprehension
        for employee in employees
    }