import cv2
import numpy as np
import paho.mqtt.client as mqtt

MQTT_BROKER = "192.168.137.70"
MQTT_PORT = 1883
COUNT_TOPIC = "person_count"

PROTOTXT = "models/MobileNetSSD_deploy.prototxt"
MODEL = "models/MobileNetSSD_deploy.caffemodel"

CLASSES = [
    "background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow",
    "diningtable", "dog", "horse", "motorbike", "person",
    "pottedplant", "sheep", "sofa", "train", "tvmonitor"
]

client = mqtt.Client(client_id="RaspberryPi")
net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
cap = None

try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError("Could not open webcam")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        h, w = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(
            cv2.resize(frame, (300, 300)),
            0.007843, (300, 300), 127.5
        )

        net.setInput(blob)
        detections = net.forward()
        person_count = 0

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            class_id = int(detections[0, 0, i, 1])

            if confidence > 0.5 and CLASSES[class_id] == "person":
                person_count += 1
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                x1, y1, x2, y2 = box.astype("int")

                cv2.rectangle(
                    frame, (x1, y1), (x2, y2), (0, 255, 0), 2
                )

        client.publish(COUNT_TOPIC, str(person_count))

        cv2.putText(
            frame, f"Count: {person_count}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2
        )

        cv2.imshow("Person Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    if cap is not None:
        cap.release()

    cv2.destroyAllWindows()
    client.loop_stop()
    client.disconnect()
