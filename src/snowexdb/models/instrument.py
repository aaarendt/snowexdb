import uuid
from sqlmodel import Field, Relationship
from snowexdb.models.base import Base
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from snowexdb.models.layer import Layer
    from snowexdb.models.campaign_observation import CampaignObservation

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
    layers : List[Layer]
        A relationship to the `Layer` model, with back_populates set to 
        "instrument", linking a layer measurement to the instrument
        that was used to measure it.
        This is NOT a column in the table but represents relationship only.
    campaign_observations : List[CampaignObservation]
        A relationship to the `CampaignObservation` model, with back_populates
        set to "instrument", linking campaign observations to the instrument
        that was used in that campaign.
        This is NOT a column in the table but represents relationship only.
    """
    __tablename__ = 'instruments'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str|None = Field(nullable=False, index=True)
    model: str|None = Field(nullable=True)
    specifications: str|None = Field(nullable=True)

    layers: List["Layer"] = Relationship(back_populates="instrument")
    campaign_observations: List["CampaignObservation"] = \
       Relationship(back_populates="instrument")

