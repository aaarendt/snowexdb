import uuid
from sqlmodel import Field, Relationship
from snowexdb.models.base import Base
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from snowexdb.models.instrument import Instrument
    from snowexdb.models.site import Site
    from snowexdb.models.measurement_type import MeasurementType

class Layer(Base, table=True):
    """
    Represents the layers table that holds all layers or profile data.
    A single data entry is a single value at depth in the
    snowpack and a single coordinate pair.  e.g. SMP profiles, Hand hardness,
    temperature, etc.

    Attributes
    ----------
    id : uuid.UUID
        The unique identifier for the user role, 
        generated automatically using UUID.
    depth : float
        The depth of the layer in the snowpack.
    bottom_depth : float
        The bottom depth of the layer in the snowpack.
    comments : str
        Any comments associated with the layer.
    value : str
        The value associated with the layer at the specified depth.
    instrument_id : uuid.UUID|None, optional
        A foreign key linking to the `instruments` table in the `public` schema.
        It is nullable and must be unique, allowing only one instrument
        per layer measurement.  
    instrument : Optional[Instrument]
        A relationship to the `Layer` model, with back_populates set to 
        "instrument", linking a layer measurement to the instrument
        that was used to measure it.
        This is NOT a column in the table but represents relationship only.
    """
    __tablename__ = 'layers'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    depth: float|None = Field(nullable=False, index=True)
    bottom_depth: float|None = Field(nullable=False)
    comments: str|None = Field(nullable=True)
    value: str|None = Field(default=None, nullable=False, index=True)
    instrument_id: uuid.UUID | None = Field(default=None, 
                                       foreign_key="public.instruments.id")    
    instrument: Optional["Instrument"] | None = \
                Relationship(back_populates="layers")
    site_id: uuid.UUID | None = Field(default=None, 
                                      foreign_key="public.sites.id")
    site: Optional["Site"] | None = \
                Relationship(back_populates="layers")
    measurement_type_id: uuid.UUID | None = Field(default=None, 
                                      foreign_key="public.measurement_type.id")
    measurement_type: Optional["MeasurementType"] | None = \
                Relationship(back_populates="layers")