from functions.OSM_Data_path import osm_data_path
from functions.Use_yolo import yolov7_detect
from functions.Create_OSM_Df import create_osm_df
from classes.CombinationCreator import CombinationCreator


def main():
    """
    Main function to execute the workflow.

    This function performs the following steps : 
    1. Object detection using YOLOv7 on photos.
    2. Merging OpenStreetMap (OSM) data.
    3. Creating a DataFrame from the merged OSM data.
    4. Filtering the OSM data based on specified elements.
    5. Combining rows of the filtered data.

    Returns: 
        None

    """

    
    # Perform object detection on photos using YOLOv7
    yolov7_detect("yolov7")

    # Merge OpenStreetMap (OSM) data
    merged_data = osm_data_path()
    merged_data_df = create_osm_df(merged_data)
    # Create an instance of CominationCreator
    comb_creator = CombinationCreator()
    # Define elements to filter the data
    elems = ['power', 'highway']

    # Filter the merged OSM data based on specified elements
    filtered_data = comb_creator.data_filtering(elems, merged_data_df)
    print('filtered_data:', filtered_data)
    
    # Comine rows of the filtered data
    result = comb_creator.row_combinator(chunk_size=1000)
    print('main result comb:', result)


if __name__ == "__main__":
    main()

