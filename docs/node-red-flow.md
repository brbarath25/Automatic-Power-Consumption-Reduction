# Node-RED Flow Documentation

## Overview

Node-RED is used for dashboard monitoring, MQTT communication, and automation in the Automatic Power Consumption Reduction System.

## Dashboard Features

The documented Node-RED flow includes:

- Temperature monitoring
- Humidity monitoring
- Light 1 control
- Light 2 control
- Fan 1 control
- Fan 2 control
- MQTT input and output nodes

## MQTT Topics

| Device or Data | MQTT Topic |
|---|---|
| Person count | `person_count` |
| Light 1 | `lig1` |
| Light 2 | `lig2` |
| Fan 1 | `fan1` |
| Fan 2 | `fan2` |

## Person Count Integration

The Python program publishes the detected people count to the `person_count` topic.

To display this value, configure an MQTT input node in Node-RED to subscribe to `person_count` and connect it to a suitable dashboard display.

## Automation Logic

Node-RED can use the received person count to apply occupancy-based rules and publish commands to the device topics.

The automation rules must be configured according to the project's requirements and tested with the actual hardware.

## Important Note

The repository contains a screenshot of the Node-RED flow for reference. The screenshot is not an importable Node-RED flow export. The complete flow configuration and the connection between `person_count` and the dashboard must be verified separately.
