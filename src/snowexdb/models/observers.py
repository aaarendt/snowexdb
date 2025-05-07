import uuid
from sqlmodel import Field, Relationship
from snowexdb.models.base import Base
from typing import List, TYPE_CHECKING
from snowexdb.models.site_observers import SiteObserversLink

if TYPE_CHECKING:
    from snowexdb.models.campaign_observation import CampaignObservation
    from snowexdb.models.site import Site
    
class Observer(Base, table=True):
    """
    Represents a single observer in the 'public.observers' table.

    Attributes
    ----------
    id : uuid.UUID
        The unique identifier for the observer,
        generated automatically using UUID.
    name : str|None
        The name of the observer.
    campaign_observations : List[CampaignObservation]
        A relationship to the `CampaignObservation` model, with back_populates 
        set to "observers", linking campaign observations to the observers.
        This is NOT a column in the table but represents relationship only. 
    site: List[Site]
        A relationship to the `Site` model, with back_populates 
        set to "SiteObserversLink", linking sites to the observers via a link
        table.
        This is NOT a column in the table but represents relationship only. 
    """
    __tablename__ = 'observers'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str|None = Field(nullable=False, index=True)

    campaign_observations: List["CampaignObservation"] = \
       Relationship(back_populates="observers")
    site: List["Site"] = Relationship(back_populates="observers",
                                               link_model=SiteObserversLink)