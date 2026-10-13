# System Workflow

## Overview

The Automatic Power Consumption Reduction System combines camera-based person detection, MQTT communication, and a Node-RED dashboard to support monitoring and control of electrical devices.

## Workflow Steps

### Step 1: Capture Video
A webcam captures video of the monitored area.

### Step 2: Detect People
The Python program uses OpenCV and the MobileNet SSD model to detect people in each video frame and calculate a person count.

### Step 3: Publish the Person Count
The Python program publishes the detected person count to the MQTT topic:

`person_count`

### Step 4: Receive MQTT Messages
The MQTT broker carries messages between the Python program and the configured Node-RED flow.

### Step 5: Monitor the System
Node-RED can display monitoring information through its dashboard. The provided flow screenshot includes temperature and humidity displays and controls for two lights and two fans.

### Step 6: Control Devices
The device-control topics used by the Python project are:

- `lig1` - Light 1
- `lig2` - Light 2
- `fan1` - Fan 1
- `fan2` - Fan 2

The Node-RED automation rules must be configured to use the person count and publish the appropriate device commands.

## Important Implementation Note

The current Python program publishes the person count to `person_count`. The original device-control logic publishes `on` or `off` commands to the four device topics. These are separate message flows.

For automatic operation, the Node-RED flow must connect the person-count input to the required automation rules and device outputs. Confirm the flow configuration and test the behavior before describing the system as fully automated.

## Temperature and Humidity

The Node-RED flow screenshot also shows temperature and humidity monitoring using the DHT11 sensor. The actual sensor wiring and MQTT input configuration should be verified against the working setup.

## Future Improvements

- Improve person-detection accuracy.
- Add and test person-count-based automation rules.
- Verify MQTT communication and device responses.
- Test manual dashboard controls alongside automatic control.
- Evaluate electricity savings using measured data.
