from classes.DataReader import FileDataReader
import pandas as pd


def osm_data_path():
    """
    Reads OpenStreetMap(OSM) data from multiple files and saves the merged data to a JSON file.

    Returns: 
        list or None: A list containing the merge OSM data if successful, otherwise None.
    """

    # Define the paths of the files to read
    file_paths = [
        "data/osm_point/osm_1.json",
        "data/osm_point/osm_2.json",
        "data/osm_point/osm_3.json",
        "data/osm_point/osm_4.json",
    ]

    # Create an instance of the FileDataReader class
    file_data_reader = FileDataReader(file_paths)
    
    try:
        # Load data from the files
        merged_results = file_data_reader.load_data()
        json_path = "data/osm_point/merged_results.json"
        file_data_reader.save_to_json(merged_results, json_path)
        return merged_results
    except FileNotFoundError as e:
        print(f"Erreur : {e}")
    
    return None 
