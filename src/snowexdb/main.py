from snowexdb.repositories.base_repository import BaseRepository
from snowexdb.models.instrument import Instrument
from snowexdb.models.layer import Layer

import csv

from pathlib import Path

INPUT_DIRECTORY = Path(__file__).parent / 'tests/data'


def add_layer_data():
    """
    Adds snow layer profile data to the database
    """
    instrument = add_instrument_data()
    sample_layers = INPUT_DIRECTORY / 'layers.csv'
    
    with sample_layers.open(mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            csv_data = Layer(depth = row["depth"],
                              bottom_depth = row["bottom_depth"],
                              value = row["value"],
                              comments = row["comments"], 
                              instrument_id = instrument.id)
            BaseRepository.add(csv_data)

def add_instrument_data():
    """
    Adds instrument data to the database
    """
    metadata_file = INPUT_DIRECTORY / 'metadata.csv'

    with metadata_file.open(mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            instrument = Instrument(name=row['name'],
                            model=row['model'],
                            specifications=row['specifications'])
        BaseRepository.add(instrument)
    return instrument

def main():
    add_layer_data()

if __name__ == "__main__":
    main()
   
