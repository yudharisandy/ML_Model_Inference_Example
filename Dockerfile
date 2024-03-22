# Use a base image with CUDA support
FROM nvidia/cuda:12.3.2-cudnn9-runtime-centos7

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0

# Install Python and pip
RUN apt-get install -y python3 python3-pip

# Copy the local code to the container
COPY . /app

# Install GPU dependencies
RUN pip3 install --no-cache-dir torch==1.10.0+cu113 torchvision==0.11.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

# Install CPU dependencies
RUN pip3 install --no-cache-dir ultralytics

# Command to run the application
CMD ["python3", "main.py"]