from shapely.wkt import loads


def extract_coordinates(way):
    """
    Extracts coordinates from a Well-Known Text (WKT) representation.
    
    Args: 
        way (str): The WKT representation of the geometry.
        Returns:
        tuple: A tuple containing the extracted coordinates (x, y).
               Returns (None, None) if an error occurs during extraction.
    """

    try:
        # Use Shapely to extract the coordinates
        point = loads(way)
        return point.x, point.y
    except Exception as e:
        print(f"Erreur lors de l'extraction des coordonnées : {e}")
        return None, None
