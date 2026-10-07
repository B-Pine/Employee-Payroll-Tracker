def format_currency(amount: float) -> str:
    """Format money as Rwandan francs."""
    return f"{amount:,.0f} RWF"


def read_non_empty(prompt: str) -> str:
    """Read text and reject empty input."""

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty.")


def read_positive_float(prompt: str) -> float:
    """Read a number greater than zero."""

    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value

            print("Value must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


def read_non_negative_float(
    prompt: str,
) -> float:
    """Read a number that cannot be negative."""

    while True:
        try:
            value = float(input(prompt))

            if value >= 0:
                return value

            print("Value cannot be negative.")

        except ValueError:
            print("Please enter a valid number.")


def read_positive_int(prompt: str) -> int:
    """Read an integer greater than zero."""

    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value

            print("Value must be greater than 0.")

        except ValueError:
            print(
                "Please enter a valid whole number."
            )


def read_non_negative_int(prompt: str) -> int:
    """Read an integer that cannot be negative."""

    while True:
        try:
            value = int(input(prompt))

            if value >= 0:
                return value

            print("Value cannot be negative.")

        except ValueError:
            print(
                "Please enter a valid whole number."
            )


def read_percentage(prompt: str) -> float:
    """
    Read a percentage from 0 to 100
    and convert it to decimal form.
    """

    while True:
        try:
            value = float(input(prompt))

            if 0 <= value <= 100:
                return value / 100

            print(
                "Percentage must be between "
                "0 and 100."
            )

        except ValueError:
            print(
                "Please enter a valid percentage."
            )


def print_payslip(
    payslip: dict[str, object],
) -> None:
    """Display a payslip in a readable format."""

    print("\n" + "=" * 40)
    print("PAYSLIP")
    print("=" * 40)

    print(
        f"Employee ID : "
        f"{payslip['employee_id']}"
    )

    print(
        f"Name        : "
        f"{payslip['name']}"
    )

    print(
        f"Role        : "
        f"{payslip['role']}"
    )

    print(
        "Gross Salary: "
        f"{format_currency(float(payslip['gross_salary']))}"
    )

    print(
        "Tax Rate    : "
        f"{float(payslip['tax_rate']) * 100:.2f}%"
    )

    print(
        "Tax Amount  : "
        f"{format_currency(float(payslip['tax_amount']))}"
    )

    print(
        "Net Salary  : "
        f"{format_currency(float(payslip['net_salary']))}"
    )

    print("=" * 40)

    