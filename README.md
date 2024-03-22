# YOLO Model Inference with Docker
A repository for showcasing a way to inference an object detection model (YOLO) using docker containerization technique.


## Detection Result Example
![detection-result](result/result_0.jpg)


## Inferencing YOLO

### Run the inference
The simple code for inferencing a Yolov8n model:

```
from ultralytics import YOLO
from utility import ShowResult

# Load a model
model = YOLO('./model/yolov8n.pt')  # pretrained YOLOv8n model

# Image file name
fileName = './data/dog.jpg'

# Run batched inference on a list of images
results = model(fileName)  # return a list of Results objects

# Process results list
index = 0
for result in results:
  ShowResult(result, index)
  index += 1
```
[Reference](https://docs.ultralytics.com/modes/predict/#__tabbed_1_1).

### Utility
Additional method:
```
# Functionize the show result method
def ShowResult(result, index: int):
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    result.show()  # display to screen
    result.save(filename=f'./result/result_{index}.jpg')  # save to disk
```


## Docker Related Explainations

### Briefly About Docker
Three basic components of docker:
```Dockerfile``` -> ```Image``` -> ```Container```

```Dockerfile```: Contains a blueprint of an image.
```Image```: An immutable snapshot that includes everything needed to run a container.
```Container```:  A lightweight and executable runtime instance of an image.

Before run the next few steps, make sure docker has successfully installed in your machine. If not, please refer to [this](https://docs.docker.com/engine/install/).

Nb: I used Docker Desktop for Windows.

### Create a Dockerfile

Create a ```Dockerfile``` file in the directory, and fill with the following code. 

GPU Support:
```
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
```

No GPU Support:
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

# Install Ultralytics dependencies
RUN pip install --no-cache-dir ultralytics

# Command to run the application
CMD ["python", "main.py"]
```

More complete informations can be found [here](https://docs.docker.com/reference/dockerfile/).

### Build a Dockerfile into an Image
Build a docker image from a Dockerfile could be done with the following command.

``` docker build -t yolomodel .```

Notes:
```-t yolomodel``` is the resulting image name and ``` .``` indicates the build context, which is the directory containing the Dockerfile and any files needed during the build process. In this example, the Dockerfile is assumed to be in the current directory.

### Run an Image as a Container
Can do with the following command:
``` docker run --rm --gpus all -v .:/app yolomodel```

Notes:
```-rm```: Remove the container once the code has been run.
```--gpus all```: State to run the code on all available GPU(s) in our machine.
```-v .:/app```: This flag mounts the current directory (where the docker run command is executed) to the ```/app``` directory inside the container. 
```yolomodel```: The docker image name that will be run as a container.


## Test the Solution
- Functionality Testing: Run the inference process using different input images and verify that the YOLO model detects objects accurately. Check if the detected objects match the ground truth annotations.
- Performance Testing: Measure the inference time of the YOLO model within the Docker container. Compare the performance metrics (such as inference speed) against running the model outside of Docker to ensure that Dockerization does not significantly impact performance.
- Resource Utilization Testing: Monitor the resource utilization (CPU, GPU, memory) of the Docker container during inference. Ensure that the container efficiently utilizes available resources and does not exceed resource limits
- Logging and Monitoring: Monitor the Docker container's logs and metrics to track its behavior during inference. Use logging and monitoring tools to detect errors, troubleshoot issues, and optimize performance.


## Next Step to Optimize the Solution
- Performance Optimization: Analyze the performance metrics gathered during testing and identify bottlenecks in the inference process. Optimize the YOLO model, code, and Docker configuration to improve inference speed and resource utilization.
