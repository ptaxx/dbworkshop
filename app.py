from session import Session
from model import Employee, Salary


def main():
    session = Session()

    employee = session.query(Employee).get(1)
    print(employee)

    salaries = session.query(Salary).filter(
        Salary.employee_id == employee.id
    )


if __name__ == "__main__":
    main()
