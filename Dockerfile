# Use a Python 3.11 base image
FROM python:3.11

# Install required system dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Command to run the application
CMD ["python", "run.py"]