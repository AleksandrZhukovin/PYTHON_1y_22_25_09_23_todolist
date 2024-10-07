from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class User(Base):
    __tablename__ = "user"

    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


class Project(Base):
    __tablename__ = "project"

    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="projects")


class Task(Base):
    __tablename__ = "task"

    name = Column(String, nullable=False)
    priority = Column(Integer, nullable=False, unique=True)
    deadline = Column(DateTime)
    is_done = Column(Boolean, nullable=False, default=False)
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="tasks")
    project = relationship("Project", back_populates="tasks")
