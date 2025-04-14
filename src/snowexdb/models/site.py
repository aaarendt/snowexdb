import uuid
from snowexdb.models.base import Base
from snowexdb.models.single_location import SingleLocationData
from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship

if TYPE_CHECKING:
    from snowexdb.models.layer import Layer

class Site(Base, SingleLocationData, table=True):
    """
    Table stores Site data. Does not store data values,
    it only stores the site metadata.
    """
    __tablename__ = 'sites'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str|None = Field(nullable=False, default=None)  # This can be pit_id
    description: str|None = Field(default=None)
    slope_angle: float|None = Field(default=None)
    aspect: float|None = Field(default=None)
    air_temp: float|None = Field(default=None)
    total_depth: float|None = Field(default=None)
    weather_description: str|None = Field(default=None)
    precip: str|None = Field(default=None)
    sky_cover: str|None = Field(default=None)
    wind: str|None = Field(default=None)
    ground_condition: str|None = Field(default=None)
    ground_roughness: str|None = Field(default=None)
    ground_vegetation: str|None = Field(default=None)
    vegetation_height: str|None = Field(default=None)
    tree_canopy: str|None = Field(default=None)
    site_notes: str|None = Field(default=None)
    
    layers: Optional["Layer"] | None = Relationship(back_populates="site")
