from sqlmodel import Field
from datetime import datetime
from geoalchemy2 import WKTElement, Geometry
from snowexdb.models.base import Base

class SingleLocationData(Base):
    """
    Base class for point and layer data

    Attributes
    ----------
    date : datetime
        The date and time of the observation.
    elevation : float
        The elevation of the observation (m).    
    geom : Geometry, optional
        A geometric representation of the measurement, stored as a POINT 
        type. This field uses the SQLAlchemy `Geometry` type 
        to store spatial data.
    """
   
    date: datetime = Field(default=None)
    elevation: float|None = Field(default=None)
    geom: WKTElement|None = Field(sa_type=Geometry(geometry_type="POINT"), 
                                nullable=True)
    # custom serializer for WKTElement
    class Config:
        json_encoders = {
            WKTElement: lambda v: v.desc if v is not None else None
        }