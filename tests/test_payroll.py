from emp_payroll_tracker.employee import (
    FullTimeEmployee,
)

from emp_payroll_tracker.payroll import (
    apply_tax,
    generate_payslip,
    process_payroll,
)


def test_apply_tax() -> None:
    tax = apply_tax(
        500_000,
        0.10,
    )

    assert tax == 50_000


def test_generate_payslip() -> None:
    employee = FullTimeEmployee(
        "EMP001",
        "Alice",
        500_000,
        bonus=50_000,
        tax=0.10,
    )

    payslip = generate_payslip(employee)

    assert (
        payslip["gross_salary"]
        == 550_000
    )

    assert (
        payslip["tax_amount"]
        == 55_000
    )

    assert (
        payslip["net_salary"]
        == 495_000
    )


def test_process_payroll_uses_employee_ids() -> None:
    employee = FullTimeEmployee(
        "EMP001",
        "Alice",
        500_000,
    )

    records = process_payroll(
        [employee]
    )

    assert "EMP001" in records

    assert (
        records["EMP001"]["name"]
        == "Alice"
    )

    