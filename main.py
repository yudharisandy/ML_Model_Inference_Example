# Install dependency
# pip install ultralytics

# Download the raw image
# wget https://raw.githubusercontent.com/yudharisandy/ML_Model_Inference_Example/main/dog.jpg

from ultralytics import YOLO
from utility.utility import ShowResult

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

# The result image can be seen in your root code file directory
# with the name "./result/result_0.jpg"