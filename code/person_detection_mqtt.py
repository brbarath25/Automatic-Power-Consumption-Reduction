
import cv2  # OpenCV library for image processing and webcam access
import numpy as np  # Library for numerical operations and array handling
import paho.mqtt.client as mqtt  # MQTT library to send data to other devices

# MQTT broker configuration
MQTT_BROKER = "192.168.137.70"  # IP address of the MQTT broker
MQTT_PORT = 1883  # Default MQTT communication port
COUNT_TOPIC = "person_count"  # Topic used to publish the person count

# Paths to the MobileNet SSD model files
PROTOTXT = "models/MobileNetSSD_deploy.prototxt"  # Model architecture file
MODEL = "models/MobileNetSSD_deploy.caffemodel"  # Pre-trained model weights

# List of object classes that the model can recognize
CLASSES = [
    "background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow",
    "diningtable", "dog", "horse", "motorbike", "person",
    "pottedplant", "sheep", "sofa", "train", "tvmonitor"
]

# Create an MQTT client with the ID RaspberryPi
client = mqtt.Client(client_id="RaspberryPi")

# Load the pre-trained MobileNet SSD object detection model
net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)

# Initialize the webcam variable
cap = None

try:
    # Connect to the MQTT broker
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    # Start the MQTT network loop in the background
    client.loop_start()

    # Open the default webcam (camera index 0)
    cap = cv2.VideoCapture(0)

    # Check whether the webcam opened successfully
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam")

    # Continuously capture and process webcam frames
    while True:
        # Read one frame from the webcam
        ret, frame = cap.read()

        # Stop the loop if the frame could not be captured
        if not ret:
            break

        # Get the height and width of the captured frame
        h, w = frame.shape[:2]

        # Resize the frame and convert it into a blob for the model
        blob = cv2.dnn.blobFromImage(
            cv2.resize(frame, (300, 300)),
            0.007843, (300, 300), 127.5
        )

        # Provide the processed image as input to the model
        net.setInput(blob)

        # Perform object detection on the image
        detections = net.forward()

        # Initialize the number of detected persons to zero
        person_count = 0

        # Examine each object detected by the model
        for i in range(detections.shape[2]):

            # Get the confidence score of the detected object
            confidence = detections[0, 0, i, 2]

            # Get the class ID of the detected object
            class_id = int(detections[0, 0, i, 1])

            # Count only objects classified as persons with confidence above 50%
            if confidence > 0.5 and CLASSES[class_id] == "person":
                person_count += 1  # Increase the person count by one

                # Convert the normalized bounding box into pixel coordinates
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])

                # Extract the top-left and bottom-right coordinates
                x1, y1, x2, y2 = box.astype("int")

                # Draw a green rectangle around the detected person
                cv2.rectangle(
                    frame, (x1, y1), (x2, y2), (0, 255, 0), 2
                )

        # Publish the detected person count to the MQTT topic
        client.publish(COUNT_TOPIC, str(person_count))

        # Display the total person count on the video frame
        cv2.putText(
            frame, f"Count: {person_count}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2
        )

        # Show the processed video with detection boxes
        cv2.imshow("Person Detection", frame)

        # Exit the loop when the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    # Release the webcam when the program ends
    if cap is not None:
        cap.release()

    # Close all OpenCV display windows
    cv2.destroyAllWindows()

    # Stop the MQTT background network loop
    client.loop_stop()

    # Disconnect from the MQTT broker
    client.disconnect()
