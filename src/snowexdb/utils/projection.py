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

def create_box(xmin, ymin, xmax, ymax, epsg):
    """
    Creates a bounding box in WKT format

    Args:
        xmin: minimum x coordinate
        ymin: minimum y coordinate
        xmax: maximum x coordinate
        ymax: maximum y coordinate
        epsg: integer representing the projection code

    Returns:
        bbox: WKTElement object representing the bounding box
    """
    bbox = 'SRID={}; POLYGON (({} {}, {} {}, {} {}, {} {}, {} {}))'.format(
        epsg, xmin, ymin, xmin, ymax, xmax, ymax, xmax, ymin, xmin, ymin)
    return bbox