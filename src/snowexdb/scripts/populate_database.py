import csv
import typer

from snowexdb.repositories.base_repository import BaseRepository
from snowexdb.models.instrument import Instrument
from snowexdb.models.layer import Layer
from snowexdb.models.site import Site
from snowexdb.utils.projection import create_geom
from datetime import datetime
from pathlib import Path

import logging


INPUT_DIRECTORY = Path(__file__).parent / 'resources/data'

logger = logging.getLogger(__name__)

db_populate_app = typer.Typer()


def add_layer_data():
    """
    Adds snow layer profile data to the database
    """
    instrument = add_instrument_data()
    site = add_site_data()

    sample_layers = INPUT_DIRECTORY / 'layers.csv'
    
    with sample_layers.open(mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            csv_data = Layer(depth = row["depth"],
                              bottom_depth = row["bottom_depth"],
                              value = row["value"],
                              comments = row["comments"], 
                              instrument_id = instrument.id,
                              site_id = site.id)
            BaseRepository.add(csv_data)
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

def add_site_data():
    """
    Adds site data to the database
    """
    metadata_file = INPUT_DIRECTORY / 'metadata.csv'

    with metadata_file.open(mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            coordinates = create_geom({"epsg":4326,
                                      "longitude":row['longitude'],
                                      "latitude":row['latitude']})
            site = Site(name=row['site_name'], 
                        elevation=400,
                        date = datetime.strptime(row['date'], '%m-%d-%Y'),
                        geom=coordinates['geom'])
        BaseRepository.add(site)    
    logger.info("Site Added Successfully")
    return site

@db_populate_app.command(help="Command to add layer data to the database")
def add_layer():
    add_layer_data()

@db_populate_app.command(help="Add site data to the database")
def add_site():
    add_site_data()