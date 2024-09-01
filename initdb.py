from model import Employee, Base, Department
from session import engine, Session


def main():
    Base.metadata.create_all(engine)
    session = Session()

    employee = Employee(first_name="Sam", last_name="Brown")

    departments = [
        Department(name="Engineering"),
        Department(name="Sales"),
        Department(name="Marketing"),
        Department(name="IT"),
        Department(name="HR"),
        Department(name="PR"),
        Department(name="Support"),
    ]

    session.add_all(departments)
    session.add(employee)
    session.commit()


if __name__ == "__main__":
    main()
