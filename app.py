from session import Session
from model import Employee


def main():
    session = Session()

    query = session.query(Employee)

    result = query.all()
    print(result)


if __name__ == "__main__":
    main()
