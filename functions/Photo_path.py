from classes.PhotoParser import PhotoParser


def photo_path():
    """
    Loads images from specified paths using PhotoParser

    Returns: 
        list: A list of dictionaries, each containing an image and its corresponding path.
    """
    # Create an instance of PhotoParser
    photo_parser = PhotoParser()
    
    # Location 1 : 3 photos
    L1_img1_path = 'data/location1/1.png'
    L1_img2_path = 'data/location1/2.png'
    L1_img3_path = 'data/location1/3.png'

    L1_img1 = photo_parser.load_image(L1_img1_path)
    L1_img2 = photo_parser.load_image(L1_img2_path)
    L1_img3 = photo_parser.load_image(L1_img3_path)

    # Location 2 : 3 photos
    L2_img1_path = 'data/location2/1.png'
    L2_img2_path = 'data/location2/2.png'
    L2_img3_path = 'data/location2/3.png'

    L2_img1 = photo_parser.load_image(L2_img1_path)
    L2_img2 = photo_parser.load_image(L2_img2_path)
    L2_img3 = photo_parser.load_image(L2_img3_path)

    # Location 3 : 1 photo
    L3_img1_path = 'data/ursulines.png'
    L3_img1 = photo_parser.load_image(L3_img1_path)
    
    # Save image paths in a list of dictionaries with images
    photo_paths_list = [{'image': L1_img1, 'path': L1_img1_path},
                        {'image': L1_img2, 'path': L1_img2_path},
                        {'image': L1_img3, 'path': L1_img3_path},
                        {'image': L2_img1, 'path': L2_img1_path},
                        {'image': L2_img2, 'path': L2_img2_path},
                        {'image': L2_img3, 'path': L2_img3_path},
                        {'image': L3_img1, 'path': L3_img1_path}]

    return photo_paths_list


