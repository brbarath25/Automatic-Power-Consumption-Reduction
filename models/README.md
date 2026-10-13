# Machine Learning Models

This folder contains the MobileNet SSD model files used for person detection.

## Required Files

- `MobileNetSSD_deploy.prototxt`: Defines the model architecture.
- `MobileNetSSD_deploy.caffemodel`: Contains the trained model weights.

## Usage

The Python program loads these files using OpenCV's deep neural network module to detect people in webcam frames.

## Notes

- Keep both model files in this folder.
- The filenames must match those used in `person_detection_mqtt.py`.
- Model compatibility and person-detection accuracy should be verified by testing the program.
