from model import Employee, Department, Hashtag, Post
from session import Session
from sqlalchemy.exc import IntegrityError


def main():
    session = Session()

    employee = session.query(Employee).get(1)
    print(employee)

    for department in employee.departments:
        print(department)

    department = session.query(Department).get(1)
    print(department)
    for employee in department.employees:
        print(employee)

    hashtag = Hashtag(name="java")
    post = Post(title="Java post", content="Java is not cool", author_id=1)

    post.hashtags.append(hashtag)

    session.add(post)

    try:
        session.commit()
    except IntegrityError:
        session.rollback()


if __name__ == "__main__":
    main()
