from sqlalchemy import create_engine , Column , Integer , String
from sqlalchemy.orm import declarative_base
db_url = "sqlite:///data.db"

engine = create_engine(db_url)

Base = declarative_base()


class  User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    
Base.metadata.create_all(engine)
    