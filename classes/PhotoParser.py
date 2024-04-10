import cv2
from classes.Yolov7Tools import Yolov7Tools
import os


class PhotoParser:
    """
    A class to parse photos and perform YOLOv7 object detection.
    """
    def __init__(self, model_path=None):
        """
        Initializes the PhotoParser object.

        Args:
            model_path (str, optional): The path to the YOLOv7 model. Defaults to None.
        """

        self.model = None

        if model_path:
            # Load the model from the specified path
            self.load_model(model_path)

    @staticmethod
    def load_image(image_path):
        """
        Loads an image from the specified path.

        Args:
            image_path (str): The path to the image file.

        Returns:
            ndarray: The loaded image as a NumPy array.
        """
        # Load the image from the file
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        # Extract the file name from the path
        file_name = os.path.basename(image_path)
        # Display the image
        cv2.imshow(file_name, image)
        # Wait for a key press to close the window
        cv2.waitKey(10000)
        # Close the window after a key press
        cv2.destroyAllWindows()
        print('image', image)
        return image
    
    @staticmethod
    def process_yolov7(images_paths_list, yolov7_path):
        """
        Processes images using YOLOv7 object detection.

        Args:
            images_paths_list (list): A list of dictionaries containing image paths and images.
            yolov7_path (str): The path to the YOLOv7 model.

        Returns:
            dict: The result of YOLOv7 object detection.
        """
        # Create an instance of YOLOv7Tools
        yolov7_tools = Yolov7Tools(yolov7_path)
        # Set the list of image paths to be processed
        yolov7_tools.set_image_paths_list(images_paths_list)
        # Download YOLOv7 weights
        yolov7_tools.download_yolov7_weights()
        # Run detection on multiple images and get the result
        result_process = yolov7_tools.run_detection_multiple_images()

        return result_process


   