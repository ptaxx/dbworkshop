import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv(".env")

DATABASE = os.environ["MYSQL_DATABASE"]
HOST = os.environ["MYSQL_HOST"]
PORT = os.environ["MYSQL_PORT"]
USER = os.environ["MYSQL_USER"]
PASSWORD = os.environ["MYSQL_PASSWORD"]

URI = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(URI)
Session = sessionmaker(bind=engine)
