from typing import TypeVar, Type
from sqlmodel import Session, SQLModel, select
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
    
    @classmethod
    def select_all(cls, from_table: Type[T]) -> list[T]:
        with Session(BaseRepository.repository_engine) as session:
            statement = select(from_table)
            results = session.exec(statement)
            return results.all()
        
    @classmethod
    def spatial_select(cls, from_table: Type[T], bbox) -> list[T]:
        with Session(BaseRepository.repository_engine) as session:
            statement = select(from_table). \
            where(from_table.geom.ST_Within(bbox))
            results = session.exec(statement)
            return results.all()
        
