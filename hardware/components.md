# Hardware Components

## Overview

The Automatic Power Consumption Reduction System is designed to support occupancy-based control of electrical appliances in classrooms, laboratories, and other buildings.

## Components and Their Roles

| Component | Purpose |
|---|---|
| Raspberry Pi | Runs the person-detection program, if used in the implementation |
| Webcam | Captures room images for person detection |
| Relay module | Switches electrical appliances through a suitable control circuit |
| Lights | Appliances targeted for automatic control |
| Fans | Appliances targeted for automatic control |
| ESP8266 / ESP32 | Provides device connectivity and control, if used |
| DHT11 sensor | Measures temperature and humidity |
| Connecting wires | Connects components in the circuit |
| Suitable power supply | Supplies the required power to the hardware |

## Software and Communication

- Python and OpenCV for person detection
- MobileNet SSD for object detection
- MQTT for message communication
- Node-RED for dashboard monitoring and automation

## Safety Considerations

- Use a relay module suitable for the connected load.
- Ensure proper insulation and electrical isolation.
- Mains electrical wiring should be handled by a qualified person.
- Verify all hardware connections before powering the circuit.

## Implementation Note

The exact hardware configuration depends on the components used in the physical implementation. The listed components and their connections must be verified against the actual circuit before deployment.
