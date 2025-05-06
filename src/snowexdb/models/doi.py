import uuid
from sqlmodel import Field, Relationship
from snowexdb.models.base import Base
from typing import List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from snowexdb.models.campaign_observation import CampaignObservation
    from snowexdb.models.site import Site

class DOI(Base, table=True):
    """
    Represents a single instrument in the 'public.instruments' table.

    Attributes
    ----------
    id : uuid.UUID
        The unique identifier for the instrument,
        generated automatically using UUID.
    doi : str|None
        The DOI of the observation.
    date_accessed: datetime|None
        The date at which the DOI was accessed.
    campaign_observations : List[CampaignObservation]
        A relationship to the `CampaignObservation` model, with back_populates 
        set to "doi", linking campaign observations to the DOI.
        This is NOT a column in the table but represents relationship only. 
    site: List[Site]
        A relationship to the `Site` model, with back_populates 
        set to "doi", linking sites to the doi.
        This is NOT a column in the table but represents relationship only.
    """
    __tablename__ = 'dois'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    doi: str|None = Field(nullable=False, index=True)
    date_accessed: datetime = Field(default=None)

    campaign_observations: List["CampaignObservation"] = \
       Relationship(back_populates="doi")
    site: List["Site"] =  Relationship(back_populates="doi")
