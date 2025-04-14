from geoalchemy2.elements import WKTElement

def create_geom(coordinates):
    """
    Adds the WKBElement to the dictionary

    Args:
        info: Dictionary containing longitude and latitude keys
        epsg: integer representing the projection code

    Returns:
        info: Dictionary containing everything it originally did plus a geom
              key with WKTElement value
    """
    # Add a geometry entry
    coordinates['geom'] = WKTElement('SRID={}; POINT({} {})'
                              ''.format(coordinates['epsg'], 
                                        coordinates['longitude'],
                                        coordinates['latitude']),
                                        extended=True)
    return coordinates
