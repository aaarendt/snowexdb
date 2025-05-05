import earthaccess

def NSIDC_access(doi):
    """
    Accesses data from NSIDC using the earthaccess library

    Args:
        doi (str): The DOI of the dataset to access.
        
    Returns:
        collections: a collections data layer
    """
    collections = earthaccess.search_data(
        doi = doi,
    )
    return collections
