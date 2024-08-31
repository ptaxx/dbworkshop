from model import Employee, Salary
from session import Session


def main():
    session = Session()

    employee = session.query(Employee).get(1)
    print(employee)

    # salaries = session.query(Salary).filter(
    #     Salary.employee_id == employee.id
    # )
    # for salary in salaries:
    #     print(salary)

    employee.salaries.append(
        Salary(amount=50000, bonus=5000, comments="Annual bonus")
    )
    # employee.pay(
    #     amount=10000,
    #     bonus=1000,
    #     comments="Monthly salary",
    # )
    session.commit()

    for salary in employee.salaries:
        print(salary)


if __name__ == "__main__":
    main()
