import uuid
from sqlmodel import Field
from snowexdb.models.base import Base

class SiteObserversLink(Base, table=True):
    """
    Link table creating many-to-many relationship between sites and observers.
    
    Attributes
    ----------
    observers_id: uuid.UUID
        Foreign key to the observers table.
    site_id: uuid.UUID
        Foreign key to the site table.
    """
    __tablename__ = 'site_observers'

    observers_id: uuid.UUID | None = Field(default=None, 
                                       foreign_key="public.observers.id",
                                       primary_key=True)
    site_id: uuid.UUID | None = Field(default=None, 
                                       foreign_key="public.sites.id",
                                       primary_key=True)
