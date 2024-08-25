from model import Employee, Base
from session import engine, Session


def main():
    Base.metadata.create_all(engine)
    session = Session()

    employee = Employee(first_name="Sam", last_name="Brown")

    session.add(employee)
    session.commit()


if __name__ == "__main__":
    main()
