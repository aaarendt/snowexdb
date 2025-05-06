import uuid
from sqlmodel import Field, Relationship
from snowexdb.models.base import Base
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from snowexdb.models.campaign_observation import CampaignObservation
    from snowexdb.models.layer import Layer

class MeasurementType(Base, table=True):
    """
    Represents a single campaign in the 'public.campaigns' table.

    Attributes
    ----------
    id : uuid.UUID
        The unique identifier for the instrument,
        generated automatically using UUID.
    name : str|None
        The name of the campaign.
    units: str|None
        The units of measurement for the campaign.
    derived: bool|None = Field()
        TRUE if the measurement type is derived
        FALSE if the measurement type is not derived
    campaign_observations : List[CampaignObservation]
        A relationship to the `CampaignObservation` model, with back_populates 
        set to "measurement_type", linking campaign observations to the 
        measurement type.
        This is NOT a column in the table but represents relationship only. 
    layer: List[Layer]
        A relationship to the `Layer` model, with back_populates 
        set to "measurement_type", linking layers to the measurement type.
        This is NOT a column in the table but represents relationship only. 
    """
    __tablename__ = 'measurement_type'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str|None = Field(nullable=False, index=True)
    units: str|None = Field()
    derived: bool|None = Field(default=False)

    campaign_observations: List["CampaignObservation"] = \
       Relationship(back_populates="measurement_type")
    layers: List["Layer"] = Relationship(back_populates="measurement_type")
