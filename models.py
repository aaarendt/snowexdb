import uuid
from sqlmodel import Field, Relationship
from snowexdb.models.base import Base
from typing import Optional

class Layer(Base, table=True):

    __tablename__ = 'layers'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    depth: float|None = Field(nullable=False, index=True)
    bottom_depth: float|None = Field(nullable=False)
    comments: str|None = Field(nullable=True)
    value: str|None = Field(default=None, nullable=False, index=True)
    
    instrument_id: uuid.UUID | None = Field(default=None, 
                                       foreign_key="public.instruments.id")
    instrument: Optional["Instrument"] | None = Relationship(back_populates="layers")


class Instrument(Base, table=True):

    __tablename__ = 'instruments'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str|None = Field(nullable=False, index=True)
    model: str|None = Field(nullable=True)
    specifications: str|None = Field(nullable=True)
    layers: Optional["Layer"] = Relationship(back_populates="instrument")