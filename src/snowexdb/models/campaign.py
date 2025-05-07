import uuid
from sqlmodel import Field, Relationship
from snowexdb.models.base import Base
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from snowexdb.models.campaign_observation import CampaignObservation
    from snowexdb.models.site import Site

class Campaign(Base, table=True):
    """
    Represents a single campaign in the 'public.campaigns' table.

    Attributes
    ----------
    id : uuid.UUID
        The unique identifier for the instrument,
        generated automatically using UUID.
    name : str|None
        The name of the campaign.
    description: str|None
        The description of the campaign.
    campaign_observations : List[CampaignObservation]
        A relationship to the `CampaignObservation` model, with back_populates 
        set to "campaign", linking campaign observations to the campaign.
        This is NOT a column in the table but represents relationship only. 
    site: List[Site]
        A relationship to the `Site` model, with back_populates 
        set to "campaign", linking sites to the campaign.
        This is NOT a column in the table but represents relationship only. 
    """
    __tablename__ = 'campaigns'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str|None = Field(nullable=False, index=True)
    description: str|None = Field()
    
    campaign_observations: List["CampaignObservation"] = \
       Relationship(back_populates="campaign")
    site: List["Site"] =  Relationship(back_populates="campaign")
