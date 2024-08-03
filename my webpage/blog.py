from sqlalchemy import create_engine ,Column ,String , Integer
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///blog.db"

blog_engine = create_engine(db_url)
Base = declarative_base()

class Blog(Base):
    __tablename__ = "Blog"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    

Base.metadata.create_all(blog_engine)
    