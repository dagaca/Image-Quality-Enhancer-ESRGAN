"""
This module provides the functionality to load the Real-ESRGAN model for image upscaling.
It retrieves model paths and device configurations from environment variables to allow
scalable and customizable model deployment.
"""
import os
import torch
from dotenv import load_dotenv
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

# Load environment variables from .env
load_dotenv()

# Load model path from .env and set the device
MODEL_PATH = os.getenv('MODEL_PATH', './models/RealESRGAN_x4plus.pth')
DEVICE_STR = os.getenv('DEVICE', 'cuda' if torch.cuda.is_available() else 'cpu')

# Ensure that DEVICE_STR is either 'cuda' or 'cpu'
if DEVICE_STR not in ['cuda', 'cpu']:
    raise RuntimeError(f"Invalid device string: '{DEVICE_STR}'")

# Set the device based on the environment variable
DEVICE = torch.device(DEVICE_STR)

# Function to load the Real-ESRGAN model
def load_esrgan_model(scale=4):
    """
    Loads the Real-ESRGAN model with the given scale factor.

    Parameters:
    - scale (int): The upscaling factor for the model. Default is 4x.

    Returns:
    - upscaler (RealESRGANer): The initialized Real-ESRGAN model.
    """
    # Define the RRDBNet architecture
    model = RRDBNet(
        num_in_ch=3,
        num_out_ch=3,
        num_feat=64,
        num_block=23,
        num_grow_ch=32,
        scale=scale
    )
    # Initialize the RealESRGANer with the loaded model and environment configurations
    upscaler = RealESRGANer(
        scale=scale,
        model_path=MODEL_PATH,
        model=model,
        tile=0,
        tile_pad=10,
        pre_pad=0,
        half=False,  # Set to True if using half-precision on CUDA
        device=DEVICE
    )
    return upscaler
