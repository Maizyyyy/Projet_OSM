from functions.Photo_path import photo_path
import cv2
from classes.PhotoParser import PhotoParser
import pandas as pd
from functions.Latest_info_yolov7 import get_latest_info


def yolov7_detect(yolov7_path):
    """
    Function to perform YOLOv7 detection on images.

    Args:
        yolov7_path (str): Path to the YOLOv7 directory.

    Returns:
        dict: A dictionary containing information about the detected objects.
    """
    # Fetch the latest information about YOLOv7
    owner = 'WongKinYiu'
    repo = 'yolov7'
    get_latest_info(owner, repo)

    # Call the function to fetch paths of images
    images_paths_list = photo_path()
    # Wait for a key press before continuing
    cv2.waitKey(0)
    # Create an instance of PhotoParser
    photo_parser = PhotoParser()
    
    # Process YOLOv7 for each location
    result_info = photo_parser.process_yolov7(images_paths_list, yolov7_path)

    print('main result:', result_info)
