import uuid
from sqlmodel import Field, Relationship
from snowexdb.models.single_location import SingleLocationData
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from snowexdb.models.campaign_observation import CampaignObservation

class Point(SingleLocationData, table=True):
    """
    Represents the points table that holds all the point data.

    Attributes
    ----------
    id : uuid.UUID
        The unique identifier for the user role, 
        generated automatically using UUID.
    version_number : int|None
        The version number of the point observation.
    equipment : str|None
        The equipment used to measure the point observation.
    units : str|None
        The units of the point observation.
    value : str|None
        The value of the point observation, stored as a string.
    campaign_observation_id: uuid.UUID
        Foreign key to the CampaignObservation table.
    campaign_observation : Optional[CampaignObservation]
        A relationship to the `CampaignObservation` model, with back_populates set to 
        "points", linking a layer measurement to the campaign observation
        that was used to measure it.
        This is NOT a column in the table but represents relationship only.
    """
    __tablename__ = 'points'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    version_number: int|None = Field(default=None)
    equipment: str|None = Field(nullable=True)
    units: str|None = Field(nullable=True)
    value: str|None = Field(default=None, nullable=False, index=True)
    campaign_observation_id: uuid.UUID | None = Field(default=None, 
                                foreign_key="public.campaign_observations.id")
    campaign_observations: Optional["CampaignObservation"] = \
       Relationship(back_populates="point_campaign")