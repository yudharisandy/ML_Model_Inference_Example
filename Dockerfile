# Use a base image with Python 3.10.14 and necessary dependencies
FROM python:3.10.14-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0

# Copy the local code to the container
COPY . /app

# Install CPU dependencies
RUN pip install --no-cache-dir ultralytics

# Install GPU dependencies
RUN pip install --no-cache-dir torch torchvision cudatoolkit=11.4 -f https://download.pytorch.org/whl/cu114/torch_stable.html

# Command to run the application
CMD ["python", "main.py"]
