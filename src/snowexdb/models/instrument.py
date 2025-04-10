import uuid
from sqlmodel import Field, Relationship
from snowexdb.models.base import Base
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from snowexdb.models.layer import Layer

class Instrument(Base, table=True):
    """
    Represents a single instrument in the 'public.instruments' table.

    Attributes
    ----------
    id : uuid.UUID
        The unique identifier for the instrument,
        generated automatically using UUID.
    name : str|None
        The name of the instrument.
    model: str|None
        The instrument model.
    specifications: str|None
        Additional specifications describing the instrument.
    layers : Optional[Layer]
        A relationship to the `Layer` model, with back_populates set to 
        "instrument", linking a layer measurement to the instrument
        that was used to measure it.
        This is NOT a column in the table but represents relationship only.
    """
    __tablename__ = 'instruments'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str|None = Field(nullable=False, index=True)
    model: str|None = Field(nullable=True)
    specifications: str|None = Field(nullable=True)
    layers: Optional["Layer"] = Relationship(back_populates="instrument")

