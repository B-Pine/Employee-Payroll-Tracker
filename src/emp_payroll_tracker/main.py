from .employee import (
    ContractEmployee,
    Employee,
    FullTimeEmployee,
    Intern,
)

from .payroll import (
    generate_payslip,
    process_payroll,
)

from .utils import (
    format_currency,
    print_payslip,
    read_non_empty,
    read_non_negative_float,
    read_non_negative_int,
    read_percentage,
    read_positive_float,
    read_positive_int,
)


def employee_exists(
    employees: list[Employee],
    employee_id: str,
) -> bool:
    """Check whether an employee ID already exists."""

    return any(
        employee.employee_id == employee_id
        for employee in employees
    )


def find_employee(
    employees: list[Employee],
    employee_id: str,
) -> Employee | None:
    """Find an employee using their ID."""

    for employee in employees:
        if employee.employee_id == employee_id:
            return employee

    return None


def add_employee(
    employees: list[Employee],
) -> None:
    """Create and store a new employee."""

    print("\nEmployee Type")
    print("1. Full-time")
    print("2. Contract")
    print("3. Intern")

    employee_type = input(
        "Choose employee type: "
    ).strip()

    if employee_type not in {"1", "2", "3"}:
        print("Invalid employee type.")
        return

    employee_id = read_non_empty(
        "Employee ID: "
    )

    if employee_exists(
        employees,
        employee_id,
    ):
        print(
            "An employee with that ID "
            "already exists."
        )
        return

    name = read_non_empty(
        "Employee name: "
    )

    salary_prompts = {
        "1": "Monthly base salary (RWF): ",
        "2": (
            "Agreed contract salary "
            "for full period (RWF): "
        ),
        "3": "Intern stipend (RWF): ",
    }

    salary = read_positive_float(
        salary_prompts[employee_type]
    )

    bonus = read_non_negative_float(
        "Bonus (RWF): "
    )

    tax = read_percentage(
        "Tax rate (%): "
    )

    if employee_type == "1":
        employee = FullTimeEmployee(
            employee_id,
            name,
            salary,
            bonus,
            tax,
        )

    elif employee_type == "2":
        contract_days = read_positive_int(
            "Total contract days: "
        )

        while True:
            days_worked = read_non_negative_int(
                "Days worked: "
            )

            if days_worked <= contract_days:
                break

            print(
                "Days worked cannot exceed "
                "contract days."
            )

        employee = ContractEmployee(
            employee_id,
            name,
            salary,
            contract_days,
            days_worked,
            bonus,
            tax,
        )

    else:
        transport_allowance = (
            read_non_negative_float(
                "Transport allowance (RWF): "
            )
        )

        employee = Intern(
            employee_id,
            name,
            salary,
            transport_allowance,
            bonus,
            tax,
        )

    employees.append(employee)

    print(
        f"Employee added successfully: "
        f"{employee}"
    )


def display_employees(
    employees: list[Employee],
) -> None:
    """Display all employees."""

    if not employees:
        print(
            "\nNo employees have been added."
        )
        return

    print("\nEMPLOYEES")
    print("-" * 60)

    for employee in employees:
        print(
            f"{employee.employee_id:<10}"
            f"{employee.name:<20}"
            f"{employee.__class__.__name__:<22}"
        )


def run_payroll(
    employees: list[Employee],
    payroll_records: dict[
        str,
        dict[str, object],
    ],
) -> None:
    """Process payroll for every employee."""

    if not employees:
        print(
            "\nAdd at least one employee "
            "before processing payroll."
        )
        return

    payroll_records.clear()

    payroll_records.update(
        process_payroll(employees)
    )

    print(
        f"\nPayroll processed for "
        f"{len(employees)} employee(s)."
    )


def show_employee_payslip(
    employees: list[Employee],
    payroll_records: dict[
        str,
        dict[str, object],
    ],
) -> None:
    """Find an employee and display a payslip."""

    employee_id = read_non_empty(
        "Enter employee ID: "
    )

    employee = find_employee(
        employees,
        employee_id,
    )

    if employee is None:
        print("Employee not found.")
        return

    payslip = generate_payslip(employee)

    payroll_records[
        employee.employee_id
    ] = payslip

    print_payslip(payslip)


def display_payroll_report(
    payroll_records: dict[
        str,
        dict[str, object],
    ],
) -> None:
    """Display payroll records."""

    if not payroll_records:
        print(
            "\nNo payroll records available. "
            "Process payroll first."
        )
        return

    print("\nPAYROLL REPORT")
    print("-" * 85)

    print(
        f"{'ID':<10}"
        f"{'Name':<20}"
        f"{'Role':<22}"
        f"{'Gross':>15}"
        f"{'Net':>15}"
    )

    print("-" * 85)

    for record in payroll_records.values():
        print(
            f"{str(record['employee_id']):<10}"
            f"{str(record['name']):<20}"
            f"{str(record['role']):<22}"
            f"{format_currency(float(record['gross_salary'])):>15}"
            f"{format_currency(float(record['net_salary'])):>15}"
        )


def print_menu() -> None:
    """Display the application's main menu."""

    print("\n" + "=" * 40)
    print("EMPLOYEE PAYROLL TRACKER")
    print("=" * 40)

    print("1. Add employee")
    print("2. View employees")
    print("3. Process payroll")
    print("4. View employee payslip")
    print("5. View payroll report")
    print("6. Exit")


def main() -> None:
    """Run the Employee Payroll Tracker."""

    employees: list[Employee] = []

    payroll_records: dict[
        str,
        dict[str, object],
    ] = {}

    while True:
        print_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":
            add_employee(employees)

        elif choice == "2":
            display_employees(employees)

        elif choice == "3":
            run_payroll(
                employees,
                payroll_records,
            )

        elif choice == "4":
            show_employee_payslip(
                employees,
                payroll_records,
            )

        elif choice == "5":
            display_payroll_report(
                payroll_records
            )

        elif choice == "6":
            print(
                "Thank you for using "
                "Employee Payroll Tracker."
            )
            break

        else:
            print(
                "Invalid option. "
                "Choose between 1 and 6."
            )


if __name__ == "__main__":
    main()
    