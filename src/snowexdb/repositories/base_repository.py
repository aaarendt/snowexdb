from typing import TypeVar
from sqlmodel import Session, SQLModel
from snowexdb.repositories import engine

T = TypeVar("T", bound=SQLModel)

class BaseRepository:
    repository_engine = engine

    @classmethod
    def add(cls, entity: T) -> T:
        with Session(BaseRepository.repository_engine) as session:
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity