import cv2
import tensorflow as tf
import numpy as np
import winsound
from datetime import datetime
import requests

# ----------------------------
# Load Trained CNN Model
# ----------------------------
model = tf.keras.models.load_model("models/forest_fire_cnn.h5")

# ----------------------------
# Alarm Control
# ----------------------------
alarm_on = False
fire_counter = 0
FIRE_THRESHOLD = 10        # Frames
CONFIDENCE_THRESHOLD = 0.8 # Confidence > 80%

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("fire_alerts.log", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def start_alarm():
    global alarm_on
    if not alarm_on:
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
        log_event("🔥 FIRE DETECTED - alarm started!")
        alarm_on = True

def stop_alarm():
    global alarm_on
    if alarm_on:
        winsound.PlaySound(None, winsound.SND_PURGE)
        log_event("✅ No fire - alarm stopped.")
        alarm_on = False

# ----------------------------
# Try to open live MJPEG stream
# ----------------------------
url = "http://192.168.100.80:8080/video"
cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print("Cannot open live MJPEG stream, switching to snapshot mode...")
    use_snapshot = True
else:
    use_snapshot = False

# ----------------------------
# Fire Detection Loop
# ----------------------------
while True:
    if use_snapshot:
        # Grab single frame from snapshot
        try:
            r = requests.get("http://192.168.100.80:8080/shot.jpg", timeout=5)
            img_arr = np.frombuffer(r.content, np.uint8)
            frame = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
            if frame is None:
                print("Failed to grab snapshot frame")
                continue
        except:
            print("Error fetching snapshot")
            continue
    else:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab live frame")
            continue

    # Preprocess for CNN
    img = cv2.resize(frame, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Prediction
    pred = model.predict(img, verbose=0)[0][0]

    # Fire detection logic
    if pred > CONFIDENCE_THRESHOLD:
        fire_counter += 1
        if fire_counter >= FIRE_THRESHOLD:
            start_alarm()
            label = f"🔥 FIRE DETECTED! ({pred:.2f})"
            color = (0, 0, 255)
        else:
            label = f"⚠️ Possible Fire ({fire_counter}/{FIRE_THRESHOLD})"
            color = (0, 255, 255)
    else:
        fire_counter = 0
        stop_alarm()
        label = f"✅ No Fire ({pred:.2f})"
        color = (0, 255, 0)

    # Display frame
    cv2.putText(frame, label, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow("Fire Detection", frame)

    # Quit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
if not use_snapshot:
    cap.release()
cv2.destroyAllWindows()
