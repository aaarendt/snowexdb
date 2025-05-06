from snowexdb.models.layer import Layer
from snowexdb.models.instrument import Instrument
from snowexdb.models.site import Site
from snowexdb.models.single_location import SingleLocationData
from snowexdb.models.doi import DOI
from snowexdb.models.campaign_observation import CampaignObservation
from snowexdb.models.campaign import Campaign
from snowexdb.models.measurement_type import MeasurementType
from snowexdb.models.observers import Observer
from snowexdb.models.site_observers import SiteObserversLink

# New models created should be exposed by adding to __all__. This is used by SQLModel.metadata
# https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#sqlmodel-metadata-order-matters
__all__ = [
    "Layer",
    "Instrument",
    "Site",
    "SingleLocationData",
    "DOI",
    "CampaignObservation",
    "Campaign",
    "MeasurementType",
    "Observer",
    "SiteObserversLink",
]
