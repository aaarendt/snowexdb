import uuid
from sqlmodel import Field, Relationship
from snowexdb.models.base import Base
from typing import TYPE_CHECKING, Optional
from datetime import datetime

if TYPE_CHECKING:
    from snowexdb.models.instrument import Instrument
    from snowexdb.models.doi import DOI
    from snowexdb.models.campaign import Campaign
    from snowexdb.models.measurement_type import MeasurementType
    from snowexdb.models.observers import Observer

class CampaignObservation(Base, table=True):
    """
    Information on a single campaign observation.

    Attributes
    ----------
    id : uuid.UUID
        The unique identifier for the instrument,
        generated automatically using UUID.
    name : str|None
        The name of the campaign.
    description: str|None
        The description of the campaign observation.
    date: datetime | None
        The date of the campaign observation.
    doi_id: uuid.UUID
        Foreign key to the DOI table. 
    doi : Optional[DOI]
        A relationship to the `DOI` model, with back_populates set to 
        "campaign_observations", linking a campaign observation 
        to the DOI of the observation.
        This is NOT a column in the table but represents relationship only.
    instrument_id: uuid.UUID
        Foreign key to the Instrument table.
    instrument : Optional[Instrument]
        A relationship to the `Instrument` model, with back_populates set to 
        "campaign_observations", linking a campaign observation 
        to the instrument used to measure it.
        This is NOT a column in the table but represents relationship only.
    campaign_id: uuid.UUID
        Foreign key to the Campaign table.
    campaign : Optional[Campaign]
        A relationship to the `Campaign` model, with back_populates set to 
        "campaign_observations", linking a campaign observation 
        to the campaign it belongs to.
        This is NOT a column in the table but represents relationship only.
    measurement_type_id: uuid.UUID
        Foreign key to the MeasurementType table.
    measurement_type : Optional[MeasurementType]
        A relationship to the `MeasurementType` model, with back_populates set
        to "campaign_observations", linking a campaign observation to the 
        measurement type it belongs to.
        This is NOT a column in the table but represents relationship only.
    observer_id: uuid.UUID
        Foreign key to the Observer table.
    observers : Optional[Observer]
        A relationship to the `Observer` model, with back_populates set
        to "campaign_observations", linking a campaign observation to the 
        observers.
        This is NOT a column in the table but represents relationship only.
    """
    __tablename__ = 'campaign_observations'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str|None = Field(nullable=False, index=True)
    description: str|None = Field(default=None)
    date: datetime = Field(default=None)

    doi_id: uuid.UUID | None = Field(default=None, 
                                       foreign_key="public.dois.id")    
    doi: Optional["DOI"] | None = \
         Relationship(back_populates="campaign_observations")
    
    instrument_id: uuid.UUID | None = Field(default=None, 
                                       foreign_key="public.instruments.id")
    instrument: Optional["Instrument"] | None = \
                Relationship(back_populates="campaign_observations")
    campaign_id: uuid.UUID | None = Field(default=None, 
                                       foreign_key="public.campaigns.id")
    campaign: Optional["Campaign"] | None = \
                Relationship(back_populates="campaign_observations")
    measurement_type_id: uuid.UUID | None = Field(default=None, 
                                       foreign_key="public.measurement_type.id")
    measurement_type: Optional["MeasurementType"] | None = \
                Relationship(back_populates="campaign_observations")
    observers_id: uuid.UUID | None = Field(default=None, 
                                       foreign_key="public.observers.id")
    observers: Optional["Observer"] | None = \
                Relationship(back_populates="campaign_observations")