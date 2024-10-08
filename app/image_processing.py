"""
This module provides utility functions for handling and converting images,
specifically focusing on converting image files into Base64-encoded strings.
"""
import base64

# Function to convert an image to Base64 format
def image_to_base64(image_path):
    """
    Converts the image at the given path to a Base64 encoded string.

    This function reads the image file from the specified path, converts its binary
    content into a Base64-encoded string, and returns the result. The Base64 encoding
    is useful for transferring binary data over mediums that only support text.

    Parameters:
    - image_path (str): The file path of the image to be converted.
                        It should point to a valid image file.

    Returns:
    - str: The Base64 encoded string representing the image content, which can be
           used for embedding images in text-based formats like JSON or HTML.
    """
    with open(image_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_string
