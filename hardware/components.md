# Hardware Components

## Project Overview

The Automatic Power Consumption Reduction System uses camera-based person detection and IoT-based device control to help reduce unnecessary electricity consumption in classrooms, laboratories, and other campus areas.

## Components Used

### 1. Webcam
Captures video of the monitored area. The video is processed by the person-detection program to estimate the number of people present.

### 2. Raspberry Pi
Runs the Python person-detection program and communicates with the MQTT broker to send person-count information.

### 3. ESP8266 / ESP32
Provides Wi-Fi-based communication for IoT device control. The exact board and its configuration should be confirmed according to the hardware setup.

### 4. Relay Module
Acts as a switching interface for controlling connected electrical devices. The actual relay wiring and control logic must be verified against the implemented circuit.

### 5. DHT11 Sensor
Measures temperature and humidity. These readings can be monitored through the Node-RED dashboard when the sensor and MQTT data flow are configured.

### 6. Lights and Fans
These are the devices targeted for automated control. The current project code uses the MQTT topics `lig1`, `lig2`, `fan1`, and `fan2`.

## System Notes

- The webcam and person-detection program estimate the number of people in the monitored area.
- MQTT carries messages between the system components.
- Node-RED can provide a dashboard for monitoring and device-control functions.
- Confirm the actual hardware connections, pin assignments, power requirements, and automation rules before testing.

## Electrical Safety

Mains-powered lights and fans can cause serious electric shock or fire if wired incorrectly. Do not connect or modify mains wiring while powered. Have the relay circuit and electrical connections checked by a qualified person.

## Implementation Status

The component list is based on the project presentation and the supplied software and Node-RED details. Confirm which boards and components were physically assembled and tested before marking the hardware implementation as complete.
