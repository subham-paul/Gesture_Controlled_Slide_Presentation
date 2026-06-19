# ============================================
# Gesture-Controlled Slide Presentation
# Backend: Flask + MediaPipe + OpenCV
# ============================================

import cv2
import time
import threading
import mediapipe as mp
import pyautogui

from flask import Flask, render_template, Response, jsonify

app = Flask(__name__)

# =============================
# GLOBAL CONTROL FLAGS
# =============================
camera_active = False
gesture_status = "Idle"
last_gesture_time = 0
camera_lock = threading.Lock()

# =============================
# MEDIAPIPE INITIALIZATION
# =============================
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# =============================
# CAMERA GENERATOR
# =============================
def camera_stream():
    global camera_active, gesture_status, last_gesture_time

    cap = cv2.VideoCapture(0)
    prev_x = None
    last_action_time = 0

    while camera_active:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        # Reset to Idle only if gesture timeout passed
        if time.time() - last_gesture_time > 1.2:
            gesture_status = "Idle"

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                wrist_x = hand_landmarks.landmark[
                    mp_hands.HandLandmark.WRIST
                ].x

                current_time = time.time()

                if prev_x is not None and current_time - last_action_time > 0.9:

                    if wrist_x - prev_x > 0.12:
                        pyautogui.press("right")
                        gesture_status = "➡ Next Slide"
                        last_gesture_time = current_time
                        last_action_time = current_time

                    elif prev_x - wrist_x > 0.12:
                        pyautogui.press("left")
                        gesture_status = "⬅ Previous Slide"
                        last_gesture_time = current_time
                        last_action_time = current_time

                prev_x = wrist_x

        ret, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
        )

    cap.release()


# =============================
# ROUTES
# =============================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/video_feed")
def video_feed():
    return Response(
        camera_stream(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

@app.route("/start_camera")
def start_camera():
    global camera_active
    with camera_lock:
        camera_active = True
    return jsonify({"status": "Camera Started"})

@app.route("/stop_camera")
def stop_camera():
    global camera_active, gesture_status
    with camera_lock:
        camera_active = False
        gesture_status = "Stopped"
    return jsonify({"status": "Camera Stopped"})

@app.route("/gesture_status")
def get_gesture_status():
    return jsonify({"gesture": gesture_status})


# =============================
# MAIN
# =============================
if __name__ == "__main__":
    pyautogui.FAILSAFE = False
    app.run(debug=True)
