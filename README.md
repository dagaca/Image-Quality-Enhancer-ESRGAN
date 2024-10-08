# 🌟 Image-Quality-Enhancer-ESRGAN

An advanced image enhancement web application powered by the Real-ESRGAN model, allowing users to upscale images with high quality. With this tool, users can upload an image, enhance it, and compare the original and processed images side-by-side for visual clarity. 

## 🎥 Project Demo

Watch the project in action! Check out the video below for a demonstration of the application's features, including image enhancement, side-by-side comparison, and download functionality.

Additionally, I've included visual comparisons of the enhanced images for better insight into the application's capabilities.

https://github.com/user-attachments/assets/4b9fd78b-01ca-41b7-b09c-51605a36f63a

![Example1](https://github.com/user-attachments/assets/06238e9f-0fa0-456b-b8f5-2ef69cf380e8)

![Example2](https://github.com/user-attachments/assets/5492a7b8-5299-4014-a1f9-faeb673c36b6)


## 📁 Project Structure

```plaintext
image-quality-enhancer-esrgan/
│
├── app/
│   ├── __init__.py            # Initializes the Flask application
│   ├── routes.py              # API routes for image enhancement
│   ├── image_enhancement.py   # Image enhancement logic and functions
│   ├── image_processing.py    # Image processing utilities
│   └── model_loader.py        # Loads the Real-ESRGAN model
│
├── config/
│   └── log_config.py          # Logging configuration for the application
│
├── models/
│   └── RealESRGAN_x4plus.pth  # Real-ESRGAN pre-trained model
│
├── templates/
│   ├── style.css              # CSS styling for the web interface
│   └── script.js              # JavaScript for frontend interactions
│   └── index.html             # HTML structure for the web interface
│
├── logs/                      # Directory for storing application logs
│   └── app.log                # Log file
│
├── .env                       # Environment variables for configuration
├── requirements.txt           # Python dependencies
└── run.py                     # Script to start the Flask application
```

## ⚙️ Getting Started

Follow these instructions to set up and run the application on your local machine.

### Installation

#### Clone the Repository

```bash
git clone https://github.com/dagaca/Image-Quality-Enhancer-ESRGAN.git
cd image-quality-enhancer-esrgan
```

#### Environment Configuration

Create a .env file in the root directory of your project with environment variables if needed. Customize the variables for your specific deployment or testing configuration.

#### Install Dependencies

Install all required Python packages using the following command:

```bash
pip install -r requirements.txt
```

#### Download the Real-ESRGAN Model

Download the pre-trained Real-ESRGAN model (`RealESRGAN_x4plus.pth`) from the [Real-ESRGAN GitHub page](https://github.com/xinntao/Real-ESRGAN). Place it in the `models/` directory.

#### Run the Application

Start the application using:

```bash
python run.py
```

The application should now be accessible at **http://127.0.0.1:5000**.

## 🌐 Usage

1. **Upload an Image**: Click on the "Select Image" button to upload an image from your computer.
2. **Choose Enhancement Option**: Select the desired enhancement:
   - **Enhance 2x**: Upscales the image to twice its original resolution.
   - **Enhance 4x**: Upscales the image to four times its original resolution.
   - **Same Size Enhance**: Improves image quality without altering its resolution.
3. **Compare Images**: Use the slider to compare the original and enhanced images side-by-side.
4. **Download Enhanced Image**: Click on "Download Enhanced Image" to save the enhanced version locally.

## 🛠️ Features

- **Image Upscaling**: Uses Real-ESRGAN to provide high-quality image upscaling.
- **Comparison Slider**: Interactive slider to compare the original and enhanced images.
- **Downloadable Output**: Enhanced images can be downloaded with a single click.
- **Robust Logging**: Logs are stored in `logs/app.log`, tracking errors and key events.

## 🔧 Configuration

The application uses a `.env` file to manage environment-specific settings. Update the `config/log_config.py` file to adjust the logging configuration as needed.

## 📝 Dependencies

Listed in `requirements.txt`, some of the core dependencies include:

- absl-py==2.1.0
- addict==2.4.0
- anyio==4.6.0
- basicsr==1.4.2
- flasgger==0.9.7.1
- Flask==2.2.5
- Flask-Cors==5.0.0
- numpy==1.24.0
- opencv-python==4.7.0.72
- Pillow==10.0.0
- requests==2.28.1
- torch==2.0.1
- torchvision==0.15.2
- realesrgan==0.3.0
- python-dotenv==0.21.0

To install all dependencies, run:

```bash
pip install -r requirements.txt
```

## 📈 Logging

Logging is configured to output to `logs/app.log`. The log configuration is managed by `log_config.py` in the `config` directory. This setup ensures all major events and errors are recorded for troubleshooting and monitoring.

## 🤝 Contributions

Contributions are welcome! To contribute:

1. **Fork the repository.**
2. **Create a new branch** for your feature or bug fix.
3. **Commit your changes** with clear and concise commit messages.
4. **Open a pull request** detailing the changes and any issues it addresses.

## 🧪 Testing

To ensure quality and performance, thoroughly test any new features or changes before submitting a pull request.

## 📄 License

This project utilizes the [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) model. The model is licensed under the [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause).
