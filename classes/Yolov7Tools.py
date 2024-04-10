import subprocess
import requests
from pathlib import Path
import json
from tqdm import tqdm


class Yolov7Tools:

    """
    A class to manage YOLOv7 for object detection on images.
    """

    def __init__(self, yolov7_local_path):
        """
        Initializes the Yolov7Tools object.

        Args:
            yolov7_local_path (str): The local path to the YOLOv7 directory.
        """
        self.yolov7_local_path = Path(yolov7_local_path)
        self.image_paths_list = None

    def set_image_paths_list(self, image_paths_list):
        """
        Sets the list of image paths to be processed.

        Args:
            image_paths_list (list): A list of dictionaries containing image paths and images.
        """
        self.image_paths_list = image_paths_list

    def download_yolov7_weights(self):
        """
        Downloads the YOLOv7 weights.
        """
        yolov7_weights_url = "https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6e.pt"
        file_name = 'yolov7-e6e.pt'

        # Try to downloading YOLOv7 weights
        try:
            response_weights = requests.get(yolov7_weights_url)
            # Raise an exception for error HTTP codes
            response_weights.raise_for_status()  
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors du téléchargement des poids du modèle YOLOv7 : {e}")
            return

        file_path = self.yolov7_local_path / file_name
        # Open file and write the data
        with open(file_path, 'wb') as weights_file:
            weights_file.write(response_weights.content)

            print(f"Les poids du modèle YOLOv7 ont été téléchargés avec succès dans : {file_path}")

    def run_detection(self, image_path):
        """
        Runs object detection on a single image.

        Args:
            image_path (str): The path to the input image.

        Returns:
            CompletedProcess: The result of the detection process.
        """
        print('local path : ', self.yolov7_local_path)
        # Define the local paths of our files
        weights_path = str(self.yolov7_local_path / 'yolov7-e6e.pt')

        # Define the output directory
        output_directory = self.yolov7_local_path/'runs'/'detect'
        # Command to execute
        command = [
            'python3', 'yolov7/detect.py',
            '--weights', str(weights_path),
            '--source', str(image_path),
            '--save-txt',
            '--save-conf',
            '--project', str(output_directory),
            '--name', 'output'
        ]
        # Use tqdm to track progress
        with tqdm(total=100, desc='Running detection') as pbar:
            # Execute the command and capture the output
            result = subprocess.run(command, capture_output=True, text=True)
            # Update the progress bar
            pbar.update(100)
        return result

    def run_detection_multiple_images(self):
        # List to store the results of each image
        results = []
        for image_info in self.image_paths_list:
            image_path = image_info['path']
            result = self.run_detection(image_path)
            results.append(result)
            print('results in yolov7Tools:', results)
        return results

