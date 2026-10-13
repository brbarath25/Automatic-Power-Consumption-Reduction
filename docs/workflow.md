# System Workflow

## Overview

The Automatic Power Consumption Reduction System combines computer vision, MQTT communication, and Node-RED to support occupancy-based energy management.

## Workflow Steps

1. **Image Capture:** A webcam captures images of the room.
2. **Person Detection:** OpenCV runs the MobileNet SSD model to detect people in the captured frames.
3. **People Counting:** The Python program counts the detected people in each frame.
4. **MQTT Communication:** The program publishes the people count to the `person_count` MQTT topic.
5. **Dashboard Monitoring:** Node-RED can subscribe to `person_count` to display the current occupancy.
6. **Automation:** Node-RED can apply rules based on occupancy and send MQTT commands to control lights and fans.
7. **Device Control:** MQTT messages use the topics `lig1`, `lig2`, `fan1`, and `fan2` for the corresponding devices.

## System Requirements

- Webcam
- Python
- OpenCV
- MobileNet SSD model files
- MQTT broker
- Node-RED
- Compatible device controllers and relay hardware for physical switching

## Important Note

The Python program publishes the detected people count to `person_count`. The Node-RED flow must be configured to subscribe to this topic and implement the required automation rules.

Hardware connections, MQTT communication, and automatic device control must be tested before the system is considered fully operational.
