# Install dependency
# pip install ultralytics

# Download the raw image
# wget https://raw.githubusercontent.com/yudharisandy/ML_Model_Inference_Example/main/dog.jpg

from ultralytics import YOLO

# Load a model
model = YOLO('./model/yolov8n.pt')  # pretrained YOLOv8n model

# Image file name
fileName = './data/dog.jpg'

# Run batched inference on a list of images
results = model(fileName)  # return a list of Results objects

# Functionize the show result method
def ShowResult(result, index: int):
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    result.show()  # display to screen
    result.save(filename=f'./result/result_{index}.jpg')  # save to disk

# Process results list
index = 0
for result in results:
  ShowResult(result, index)
  index += 1

# The result image can be seen in your root code file directory
# with the name "./result/result_0.jpg"