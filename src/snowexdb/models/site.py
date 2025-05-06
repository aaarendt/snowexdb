import uuid
from snowexdb.models.single_location import SingleLocationData
from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from snowexdb.models.site_observers import SiteObserversLink

if TYPE_CHECKING:
    from snowexdb.models.layer import Layer
    from snowexdb.models.doi import DOI
    from snowexdb.models.campaign import Campaign
    from snowexdb.models.observers import Observer
#    from snowexdb.models.site_observers import SiteObserversLink

class Site(SingleLocationData, table=True):
    """
    Table stores Site data. Does not store observed data values,
    it only stores the site metadata.

    Attributes
    ----------
    id : uuid.UUID
        The unique identifier for the user role, 
        generated automatically using UUID.
    name : str
        The name of the site.
    description : str
        A brief description of the site.
    slope_angle : float 
        The site slope angle in degrees.
    aspect : float
        The site aspect in degrees.
    air_temp : float
        The air temperature at the site (°C).
    total_depth : float
        The total depth of the snowpack (m).
    weather_description : str
        A description of the weather conditions.
    precip : str
        The precipitation type or amount.
    sky_cover : str
        The sky cover conditions.
    wind : str
        The wind conditions at the site.
    ground_condition : str
        The condition of the ground at the site.
    ground_roughness : str
        The roughness of the ground surface.
    ground_vegetation : str
        The type of vegetation on the ground.
    vegetation_height : str
        The height of the vegetation (m).
    tree_canopy : str
        The tree canopy cover percentage.
    site_notes : str
        Additional notes about the site.
    layers : Optional[Layer]
        A relationship to the `Layer` model, with back_populates set to 
        "site", linking a layer measurement to the site at which it was 
        measured.
        This is NOT a column in the table but represents relationship only. 
    doi_id: uuid.UUID
        Foreign key to the DOI table. 
    doi : Optional[DOI]
        A relationship to the `DOI` model, with back_populates set to 
        "campaign_observations", linking a campaign observation 
        to the DOI of the observation.
        This is NOT a column in the table but represents relationship only. 
    campaign_id: uuid.UUID
        Foreign key to the Campaign table.
    campaign : Optional[Campaign]
        A relationship to the `Campaign` model, with back_populates set to 
        "site", linking a site to the campaign it belongs to.
        This is NOT a column in the table but represents relationship only.  
    observers: List[Observer]
        A relationship to the `observers` model, with back_populates 
        set to "SiteObserversLink", linking sites to the observers via a link
        table.
        This is NOT a column in the table but represents relationship only.  
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
    doi_id: uuid.UUID | None = Field(default=None, 
                                       foreign_key="public.dois.id")    
    doi: Optional["DOI"] | None = Relationship(back_populates="site")
    campaign_id: uuid.UUID | None = Field(default=None, 
                                       foreign_key="public.campaigns.id")
    campaign: Optional["Campaign"] | None = Relationship(back_populates="site")
    observers: list["Observer"] = Relationship(back_populates="site",
                                               link_model=SiteObserversLink)

