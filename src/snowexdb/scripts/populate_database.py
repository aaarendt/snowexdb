import csv
import typer

from snowexdb.repositories.base_repository import BaseRepository
from snowexdb.models.instrument import Instrument
from snowexdb.models.layer import Layer
from snowexdb.models.site import Site
from snowexdb.utils.projection import create_geom
from pathlib import Path

import logging

from snowexdb.utils.data_parser import download_csv, parse_csv_data
from snowexdb.utils.access_data import NSIDC_access

INPUT_DIRECTORY = Path(__file__).parent / 'resources/data'

logger = logging.getLogger(__name__)

db_populate_app = typer.Typer()

def add_layer_data(profile_df, metadata):
    """
    Adds snow layer profile data to the database

    Args:
        profile_df (dataframe): the dataframe of observations
        metadata (object): the metadata associated with the profile data
    
    """
    instrument = add_instrument_data()
    site = add_site_data(site_metadata={"latitude": metadata.latitude,
                                        "longitude": metadata.longitude,
                                        "elevation": 400, # temporary
                                        "name":metadata.site_name,
                                        "date":metadata.date_time})

    for index, row in profile_df.iterrows():
        data = Layer(depth=row["depth"],
                          bottom_depth=row["bottom_depth"],
                          value=str(row["density"]), #temporary
                          comments=metadata.comments, 
                          instrument_id=instrument.id,
                          site_id=site.id)
        BaseRepository.add(data)
    logger.info("Layer Added Successfully")

def add_instrument_data():
    """
    Adds instrument data to the database
    """
    metadata_file = INPUT_DIRECTORY / 'metadata.csv'

    with metadata_file.open(mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            instrument = Instrument(name=row['instrument_name'],
                            model=row['instrument_model'],
                            specifications=row['instrument_specifications'])
        BaseRepository.add(instrument)    
    logger.info("Instrument Added Successfully")
    return instrument

def add_site_data(site_metadata):
    """
    Adds site data to the database

    Args:
        site_metadata (dict): dictionary of site metadata elements
    """

    coordinates = create_geom({"epsg":4326,
                                "longitude":site_metadata['longitude'],
                                "latitude":site_metadata['latitude']})
    site = Site(name=site_metadata['name'], 
                elevation=site_metadata['elevation'],
                date=site_metadata['date'],
                geom=coordinates['geom'])
    BaseRepository.add(site)    
    logger.info("Site Added Successfully")
    return site

@db_populate_app.command(help="Add density data to the database")
def add_density():
    collections = NSIDC_access("10.5067/KZ43HVLZV6G4")
    for collection in collections:
        files = collection.data_links("Data")
        for file in files:
            if "density" in file:
                download_csv(file)
                profileData = parse_csv_data(INPUT_DIRECTORY / 
                                             "downloaded_file.csv")
                for profile in profileData.profiles:
                    add_layer_data(profile.df, profile.metadata)
                print("{} file imported!".format(file))

# TODO: determine right level of loops to add the site and instrument data, 
# not for each profile object as being done now

# for temporarily testing with a single file
        #files = ["https://n5eil01u.ecs.nsidc.org/DP6/SNOWEX/SNEX20_TS_SP.002/2019.12.16/SNEX20_TS_SP_20191216_1232_COFEJ2_data_density_v02.csv"]
