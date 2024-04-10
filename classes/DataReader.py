import json


class FileDataReader:

    """
    This class reads, cleans, and saves data in JSON format.
    """

    def __init__(self, input_filepath, output_filepath=None):
        """
        Initializes the FileDataReader object.

        Args:
            input_filepath (str or list): The file path or list of file paths to read data from.
            output_filepath (str, optional): The file path to save data. Defaults to None.
        """
        self.input_filepath = input_filepath

    @staticmethod
    def read_json(file_path):
        """
        Reads JSON data from a file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The JSON data read from the file.
        """
        with open(file_path, 'r') as file:
            json_data = json.load(file)
        return json_data

    def load_data(self):
        """
        Loads data from JSON files.

        Returns:
            list: A list containing the loaded JSON data from input files.
        """
        merged_results = []
        for input_filepath in self.input_filepath:
            data = self.read_json(input_filepath)
            merged_results.append(data)
        return merged_results

    @staticmethod
    def save_to_json(data, file_path):
        """
        Saves data to a JSON file.

        Args:
            data (dict): The data to be saved.
            file_path (str): The path to the output JSON file.
        """
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)









