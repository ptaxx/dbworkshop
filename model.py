import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DECIMAL,
    Date,
    Table,
    Text,
    DateTime,
)
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    salaries = relationship("Salary", back_populates="employee")
    departments = relationship(
        "Department",
        secondary="employees_departments_mapping",
        back_populates="employees"
    )
    posts = relationship("Post", back_populates="author")

    def pay(self, amount, bonus, date=None, comments=None):
        salary = Salary(amount=amount, bonus=bonus)

        if date is not None:
            salary.date = date

        if comments is not None:
            salary.comments = comments

        self.salaries.append(salary)

    def __repr__(self):
        return f"Employee({self.id}, {self.first_name}, {self.last_name})"


class Salary(Base):
    __tablename__ = "salaries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(DECIMAL, nullable=False)
    bonus = Column(DECIMAL, nullable=False, default=0)
    date = Column(
        Date,
        nullable=False,
        default=datetime.date.today
    )
    comments = Column(String(150))

    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)

    employee = relationship("Employee", back_populates="salaries")

    def __repr__(self):
        return f"Salary({self.amount}, {self.date}, {self.employee_id})"


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    employees = relationship(
        "Employee",
        secondary="employees_departments_mapping",
        back_populates="departments"
    )

    def __repr__(self):
        return f"Department({self.id}, {self.name})"


employee_department = Table(
    "employees_departments_mapping",
    Base.metadata,
    Column(
        "employee_id",
        Integer,
        ForeignKey("employees.id"),
        primary_key=True
    ),
    Column(
        "department_id",
        Integer,
        ForeignKey("departments.id"),
        primary_key=True
    ),
)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    publication_date = Column(DateTime, default=datetime.datetime.now)
    author_id = Column(Integer, ForeignKey("employees.id"))

    hashtags = relationship(
        "Hashtag",
        secondary="posts_hashtags",
        back_populates="posts"
    )
    author = relationship("Employee", back_populates="posts")

    def __repr__(self):
        return f"Post({self.id}, {self.title})"


class Hashtag(Base):
    __tablename__ = "hashtags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

    posts = relationship(
        "Post",
        secondary="posts_hashtags",
        back_populates="hashtags"
    )

    def __repr__(self):
        return f"Hashtag({self.id}, {self.name})"


posts_hashtags = Table(
    "posts_hashtags",
    Base.metadata,
    Column(
        "post_id",
        Integer,
        ForeignKey("posts.id"),
        primary_key=True
    ),
    Column(
        "hashtag_id",
        Integer,
        ForeignKey("hashtags.id"),
        primary_key=True
    ),
)
