"""
This module provides functions to enhance image quality using the RealESRGAN model.
The enhancement can be applied with different scale factors (e.g., 2x, 4x) or to maintain 
the original image size while improving its quality.

Functions:
- open_image: Opens an image file and converts it to RGB format.
- convert_image_to_numpy: Converts a PIL Image object to a NumPy array.
- enhance_image_with_model: Enhances the image using the RealESRGAN model.
- resize_to_original: Resizes an enhanced image back to its original dimensions.
- save_enhanced_image: Saves the enhanced image to a temporary directory.
- process_image_enhancement: Main function that orchestrates the entire enhancement process.
"""
import os
import tempfile
from PIL import Image, UnidentifiedImageError
import numpy as np
from .image_processing import image_to_base64

def open_image(image_path):
    """
    Opens an image from the given path and converts it to RGB format.
    
    Parameters:
    - image_path (str): Path to the image file to open.
    
    Returns:
    - PIL.Image.Image: Image object in RGB format.
    
    Raises:
    - UnidentifiedImageError: If the file is not recognized as an image.
    """
    try:
        return Image.open(image_path).convert('RGB')
    except UnidentifiedImageError as exc:
        raise UnidentifiedImageError(f"Cannot identify image file: {image_path}") from exc

def convert_image_to_numpy(image):
    """
    Converts a PIL Image object to a NumPy array.
    
    Parameters:
    - image (PIL.Image.Image): Image object to convert.
    
    Returns:
    - np.ndarray: The image as a NumPy array.
    """
    return np.array(image)

def enhance_image_with_model(image_np, scale_factor, upscaler):
    """
    Enhances the given image using the RealESRGAN model with the specified scale factor.
    
    Parameters:
    - image_np (np.ndarray): The input image as a NumPy array.
    - scale_factor (int): The scale factor for enhancement (e.g., 2, 4).
    - upscaler: The RealESRGAN model instance for enhancement.
    
    Returns:
    - np.ndarray: The enhanced image as a NumPy array.
    """
    sr_image, _ = upscaler.enhance(image_np, outscale=scale_factor)
    return sr_image

def save_enhanced_image(sr_image, temp_dir):
    """
    Saves the enhanced image to a temporary file and returns the file path.
    
    Parameters:
    - sr_image (np.ndarray or PIL.Image.Image): The enhanced image.
    - temp_dir (str): The temporary directory where the image should be saved.
    
    Returns:
    - str: Path to the saved enhanced image.
    """
    with tempfile.NamedTemporaryFile(suffix='.png', dir=temp_dir, delete=False) as temp_file:
        output_image_path = temp_file.name
        if isinstance(sr_image, np.ndarray):
            sr_image = Image.fromarray(sr_image)
        sr_image.save(output_image_path)
    return output_image_path

def resize_to_original(sr_image, original_size):
    """
    Resizes the enhanced image back to its original dimensions.
    
    Parameters:
    - sr_image (np.ndarray or PIL.Image.Image): The enhanced image to resize.
    - original_size (tuple): The original size (width, height) of the image.
    
    Returns:
    - PIL.Image.Image: The resized image as a PIL Image object.
    """
    if isinstance(sr_image, np.ndarray):
        sr_image = Image.fromarray(sr_image)
    return sr_image.resize(original_size, Image.LANCZOS)

def process_image_enhancement(image_path, scale_factor, upscaler):
    """
    Main function that orchestrates the image enhancement process.
    
    This function opens the image, enhances it with the specified scale factor, and optionally
    resizes it back to its original dimensions if the scale factor is 1. The enhanced image is
    then saved to a temporary directory and returned as a Base64 string.
    
    Parameters:
    - image_path (str): Path to the input image.
    - scale_factor (int): The scale factor for enhancement. Use 1 for same-size enhancement.
    - upscaler: The RealESRGAN model instance for image enhancement.
    
    Returns:
    - str: Base64 encoded string of the enhanced image.
    
    Raises:
    - UnidentifiedImageError: If the input file is not recognized as a valid image.
    """
    with tempfile.TemporaryDirectory(dir=os.getcwd(), prefix='temp_') as temp_dir:
        # Open and convert the image to RGB
        image = open_image(image_path)
        # Convert image to NumPy array
        image_np = convert_image_to_numpy(image)
        # Enhance the image
        sr_image = enhance_image_with_model(image_np, scale_factor, upscaler)
        # Resize back to original size if needed
        if scale_factor == 1:
            sr_image = resize_to_original(sr_image, image.size)
        # Save the enhanced image
        output_image_path = save_enhanced_image(sr_image, temp_dir)
        # Convert to Base64 and return
        enhanced_image_base64 = image_to_base64(output_image_path)
        return enhanced_image_base64
