# YOLO Model Inference Example
A repo for showcasing a way to inference a ML model.


## Detection result 

### Raw Image
![raw-image](data/dog.jpg)

### Detection Result
![detection-result](result/result_0.jpg)


## Docker Related Explainations

### Create a Dockerfile
```
# Use a base image with Python 3.10.14 and necessary dependencies
FROM python:3.10.14-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0

# Copy the local code to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir ultralytics

# Command to run the application
CMD ["python", "main.py"]
```

### Build a Dockerfile to an image
``` docker build -t detection-app .```

### Run an image (convert to a container)
``` docker run -rm --gpus all -v .:/app model```

