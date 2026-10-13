# Node-RED Flow Documentation

## Overview

This document describes the Node-RED flow shown in the project's screenshot.

## Temperature and Humidity

The flow includes an MQTT input labelled `TH`. It connects to two function nodes, `temp` and `hum`, which feed the Temperature and Humidity dashboard displays.

## Light Controls

The dashboard contains two switches:

- **Light 1:** Associated with MQTT topic `lig1` and a function node labelled `lig1 1`.
- **Light 2:** Associated with MQTT topic `lig2` and a function node labelled `lig 2`.

The screenshot also shows audio output nodes connected to the function nodes.

## Fan Controls

The dashboard contains two switches:

- **Fan 1:** Associated with MQTT topic `fan1` and a function node labelled `fan 1`.
- **Fan 2:** Associated with MQTT topic `fan2` and a function node labelled `fan 2`.

The screenshot also shows audio output nodes connected to the function nodes.

## Dashboard

The screenshot shows two UI countdown switches, dashboard controls for the lights and fans, and temperature and humidity displays.

## Relationship to the Python Program

The Python person-detection program publishes a person count to the MQTT topic `person_count`. The screenshot does not show a `person_count` input or the complete automation logic that connects person detection to the device controls.

The integration between person-count messages and automatic device control must be configured and tested separately.

## Project File Status

This repository includes a screenshot for visual reference. The original Node-RED flow export in JSON format has not been provided, so the screenshot cannot be imported as a working Node-RED flow.
