import cv2
import os
import sys
from ultralytics import YOLO
from sort.sort import *
from plate_processing import get_car, read_license_plate, write_csv

"""
This script uses YOLO and SORT to identify vehicles and their license plates in a video.
"""

# Constants
VIDEO_FILE_PATH = "./sample.mp4"
CSV_FILE_PATH = "./frames.csv"

# Setup
results = {}
mot_tracker = Sort()  # This is the Multi-object tracker

# Load models
coco_model = YOLO('./models/yolov8n.pt')  # Model trained on the COCO dataset for object detection (in this case: all vehicle classes)
license_plate_detector = YOLO('./models/license_plates_ascensao.pt')  # Model specifically for license plate detection treined by Bernardo Ascensao

# Load video
if not os.path.exists(VIDEO_FILE_PATH):
    raise FileNotFoundError(f"Video file {VIDEO_FILE_PATH} not found.")

cap = cv2.VideoCapture(VIDEO_FILE_PATH)
if not cap.isOpened():
    print(f"Error opening video file {VIDEO_FILE_PATH}")
    sys.exit(1)

# List of all vehicle class ids in the COCO dataset:
vehicles = [2, 3, 5, 7]

# Read Frames
frame_nmr = -1
ret = True
while ret:
    frame_nmr += 1
    ret, frame = cap.read()
    if ret:
        results[frame_nmr] = {}
        # Detect Vehicles
        detections = coco_model(frame)[0]
        detections_ = []
        for detection in detections.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detection
            if int(class_id) in vehicles:
                detections_.append([x1, y1, x2, y2, score])

        # Track Vehicles
        if detections_:
            track_ids = mot_tracker.update(np.asarray(detections_))

        # Detect License Plates
        license_plates = license_plate_detector(frame)[0]

        print(f"Raw license plate detections: {license_plates}") 

        for license_plate in license_plates.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = license_plate

            # Assign license plate to car
            xcar1, ycar1, xcar2, ycar2, car_id = get_car(license_plate, track_ids)

            if car_id != -1:

                # Crop license plate
                license_plate_crop = frame[int(y1):int(y2), int(x1): int(x2), :]

                # Read license plate number
                license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop)


                if license_plate_text is not None:
                    results[frame_nmr][car_id] = {'car': {'bbox': [xcar1, ycar1, xcar2, ycar2]},
                                                  'license_plate': {'bbox': [x1, y1, x2, y2],
                                                                    'text': license_plate_text,
                                                                    'bbox_score': score,
                                                                    'text_score': license_plate_text_score}}
                    
                else:
                    print("No license plate text read from the crop")

# Write Results
if not results:
    print("No results to write to CSV")
else:
    write_csv(results, CSV_FILE_PATH)