import pandas as pd
from functions.Extract_Positions import extract_coordinates


def create_osm_df(merged_results):
    """
    Function to create a DataFrame from merged OpenStreetMap (OSM) results.

    Args:
        merged_results (list): A list of dictionaries containing merged OSM results.
    Returns:
        pandas.Dataframe: Dataframe containing extracted elements, values, latitude and longitude.
    """
    # Initialize the resulting DataFrame
    col_df = ['element', 'value', 'latitude', 'longitude']
    result_df = pd.DataFrame(columns=col_df)

    # Loop through the merged results
    for result in merged_results:
        if "planet_osm_point" in result:
            # Create a Dataframe
            osm_df = pd.DataFrame(result["planet_osm_point"])
            # Exclude the 'osm_id' column
            new_df = osm_df.drop('osm_id', axis=1)

            # Iterate through the columns and values of each row
            for _, row in new_df.iterrows():
                # Extract coordinates from the 'way' column
                latitude, longitude = extract_coordinates(row['way'])

                for col, value in row.items():
                    if value is not None:
                        # Create a DataFrame with the values
                        data_to_append = pd.DataFrame(
                            {"element": [col], "value": [value], "latitude": latitude,
                             "longitude": longitude})
                        # Check if the resulting DataFrame is empty before concatenating     
                        if result_df.empty:
                            result_df = data_to_append
                        else:
                            result_df = pd.concat([result_df, data_to_append], ignore_index=True)
        # Extract rows where the 'element' column is not equal to 'way'
        final_result = result_df[~ result_df['element'].str.contains('way')]
        # Return the Dataframe
        return final_result
