from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


URI = "mysql+mysqlconnector://root:qwerty@localhost:3306/startup"
# URI = "sqlite:///startup.db"
engine = create_engine(URI)
Session = sessionmaker(bind=engine)
