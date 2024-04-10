import pandas as pd
import glob
import os
from tqdm import tqdm
import itertools
from itertools import combinations, product
import numpy as np


class CombinationCreator:
    """
    A class to create combinations of row indices from filtered data.

    This class provides methods to filter data based on specified elements and then generate combinations
    of row indices from the filtered data.

    Attributes:
        result_dict (dict): A dictionary to store the resulting combinations.
        elements_list (list): A list to store elements for data filtering.
        parent_data (DataFrame): A DataFrame to store the parent data.
    """

    def __init__(self):
        """
        Initializes the CombinationCreator object.
        """
        self.result_dict = {}
        self.elements_list = []
        self.parent_data = pd.DataFrame()

    def data_filtering(self, elements_list, parent_data):
        """
        Filters the data based on the provided elements.

        Args:
            elements_list (list): A list of elements for data filtering.
            parent_data (DataFrame): The DataFrame containing the parent data.

        Returns:
            DataFrame: The filtered DataFrame based on the specified elements.
        """
        self.elements_list = elements_list
        self.parent_data = parent_data
        self.filtered_data = self.parent_data

        # Iterate through the row of the parent DataFrame
        for row in parent_data.iterrows():
            # Check if the first column (element) of the row is not in the list of elements to keep 
            if row[1].iloc[0] not in self.elements_list:
                # Get the index of the row
                row_index = int(row[0])
                # Drop the row from the filtered data
                self.filtered_data = self.filtered_data.drop(row_index)
        return self.filtered_data

    @staticmethod
    def chunks_data(data_list, chunk_size):
        """
        Generator function to yield chunks of data from a list.

        Args:
            data_list (list): The input list to be divided into chunks.
            chunk_size (int): The size of each chunk.

        Yields:
            list: A chunk of data from the input list.
        """
        for i in range(0, len(data_list), chunk_size):
            # Use yield to return the current chunk of data_list on each iteration
            yield data_list[i:i + chunk_size]

    def row_combinator(self, chunk_size=None):
        """
        Generates row index combinations and stores them in a dictionary.

        Args:
            chunk_size (int, optional): The size of each chunk for processing.

        Returns:
            dict: A dictionary containing the generated row index combinations.
        """
        result_dict = {}
        num_row = len(self.filtered_data)
        elements_list = list(range(num_row))

        for chunk in self.chunks_data(elements_list, chunk_size):
            for r in range(1, len(chunk) + 1):
                for combo in product(*[combinations(chunk, r) for _ in range(r)]):
                    key = tuple(sorted(combo))
                    # Convert the index into a NumpY array before indexing
                    index_array = np.array(list(key))
                    result_dict[key] = self.filtered_data.index.to_numpy()[index_array]

        print(len(result_dict))
        return result_dict
