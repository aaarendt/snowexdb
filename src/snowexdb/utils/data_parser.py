from insitupy.campaigns.snowex import SnowExProfileData
from insitupy.variables import ExtendableVariables

from insitupy.campaigns.snowex.snowex_profile_data_collection \
     import SnowExProfileDataCollection

import requests
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def download_csv(csv_url):
    """
    Download CSV file from the given URL

    Args:
        csv_url (str): the URL of the CSV file to download
    
    Output:
        downloaded_file.csv: a temporary local file that gets consistently
        overwritten after it is uploaded to the database    
    """
    response = requests.get(csv_url)
    if response.status_code == 200:
        with open(ROOT_DIR + 
                  "/scripts/resources/data/downloaded_file.csv", "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed to download the file. Status code: \
              {response.status_code}")


def parse_csv_data(fname):
    """
    Parse the CSV data from the given file name, using insitupy library.
    
    Args:
        fname (str): the name of the CSV file to parse.
    
    Returns:
        profile_data (obj): profile data object containing the observations
        and the metadata. 
    
    Unclear why primary_variable_files not working - check latest insitupy
    updates?
    """

    file_list = SnowExProfileData.DEFAULT_PRIMARY_VARIABLE_FILES + \
    ["./overrides.yaml"]
    my_vars = ExtendableVariables(file_list)
    profile_data = SnowExProfileDataCollection.from_csv(
        fname, allow_map_failure=True,
        # primary_variable_files=file_list, 
    )
    return profile_data