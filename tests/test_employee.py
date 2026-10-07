import pytest

from emp_payroll_tracker.employee import (
    ContractEmployee,
    FullTimeEmployee,
    Intern,
)


def test_full_time_salary() -> None:
    employee = FullTimeEmployee(
        "EMP001",
        "Alice",
        500_000,
        bonus=50_000,
        tax=0.10,
    )

    assert (
        employee.calculate_salary()
        == 550_000
    )


def test_contract_salary_is_prorated() -> None:
    employee = ContractEmployee(
        "EMP002",
        "Bob",
        300_000,
        contract_days=30,
        days_worked=15,
        bonus=10_000,
        tax=0.05,
    )

    assert employee.calculate_salary() == pytest.approx(
        160_000
    )


def test_intern_salary_includes_transport() -> None:
    employee = Intern(
        "EMP003",
        "Chris",
        100_000,
        transport_allowance=20_000,
        bonus=5_000,
        tax=0.0,
    )

    assert (
        employee.calculate_salary()
        == 125_000
    )


def test_salary_must_be_positive() -> None:
    with pytest.raises(ValueError):
        FullTimeEmployee(
            "EMP004",
            "Diane",
            0,
        )


def test_bonus_cannot_be_negative() -> None:
    with pytest.raises(ValueError):
        FullTimeEmployee(
            "EMP005",
            "Eric",
            200_000,
            bonus=-1,
        )


def test_tax_must_be_valid() -> None:
    with pytest.raises(ValueError):
        FullTimeEmployee(
            "EMP006",
            "Faith",
            200_000,
            tax=1.5,
        )

        