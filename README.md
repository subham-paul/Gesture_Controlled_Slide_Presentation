# 🎤 Gesture Controlled Slide Presentation

A modern **Gesture-Controlled Presentation System** built with **Python**, **Flask**, **OpenCV**, and **MediaPipe**. This application enables users to control PowerPoint or presentation slides using hand gestures captured through a webcam, eliminating the need for a traditional mouse or presentation remote.

> **Deliver presentations effortlessly with intuitive hand gestures powered by Artificial Intelligence and Computer Vision.**

---

# ✨ Features

- 🖐️ Hand gesture recognition
- 🎥 Real-time webcam tracking
- ▶️ Next and previous slide navigation
- ✍️ Virtual laser pointer *(optional)*
- 📝 Annotation support *(optional)*
- ⚡ Smooth and responsive gesture detection
- 🌐 Flask-based web interface
- 📷 Real-time video processing
- 💻 Cross-platform compatibility

---

# 🛠️ Tech Stack

## Backend

- Python 3.x
- Flask

## Computer Vision

- OpenCV
- MediaPipe

## Automation

- PyAutoGUI / Keyboard Controller *(depending on implementation)*

## Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap
- Jinja2 Templates

---

# 📂 Project Structure

```text
Gesture_Controlled_Slide_Presentation/
│
├── app.py
├── requirements.txt
├── config.py
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── slides/
│
├── templates/
│   ├── index.html
│   ├── presentation.html
│   └── ...
│
├── models/
├── utils/
├── README.md
│
└── ...
```

---

# 🚀 Features Overview

- 🖐️ AI Hand Gesture Recognition
- 🎥 Live Webcam Detection
- ⏭️ Next Slide Control
- ⏮️ Previous Slide Control
- 🖱️ Gesture-Based Navigation
- 📽️ Presentation Mode
- ⚡ Real-Time Processing
- 💻 Lightweight & Fast
- 🌐 Browser-Based Interface
- 📊 Easy to Extend

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/subham-paul/Gesture_Controlled_Slide_Presentation.git
```

```bash
cd Gesture_Controlled_Slide_Presentation
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
python app.py
```

or

```bash
flask run
```

---

# 🌐 Open in Browser

```
http://127.0.0.1:5000
```

---

# 📝 How It Works

1. Launch the application.
2. Allow access to your webcam.
3. The webcam continuously tracks your hand movements.
4. MediaPipe detects hand landmarks in real time.
5. Recognized gestures are mapped to presentation controls.
6. Slides change automatically based on the detected gesture.
7. Present without touching your keyboard or mouse.

---

# ✋ Example Gestures

| Gesture | Action |
|----------|--------|
| 👉 Swipe Right | Next Slide |
| 👈 Swipe Left | Previous Slide |
| ✋ Open Palm | Pause Detection |
| ☝️ Index Finger | Virtual Pointer |
| ✍️ Pinch Gesture | Annotation *(Optional)* |

> *Available gestures may vary depending on your implementation.*

---

# 📊 Applications

- Smart Classrooms
- Business Presentations
- Online Teaching
- Conferences & Seminars
- Training Sessions
- Interactive Learning
- AI Demonstrations
- Touchless Presentation Systems

---

# 🚀 Future Enhancements

- 🎯 AI Gesture Customization
- 📝 Whiteboard Annotation
- 🔴 Virtual Laser Pointer
- 🎤 Voice Command Integration
- 🌍 Multi-Hand Recognition
- ☁️ Cloud Presentation Support
- 📱 Mobile Controller Integration
- 🤖 Deep Learning Gesture Recognition
- 📊 Presentation Analytics
- 🌐 Remote Presentation Control

---

# 🤝 Contributing

Contributions are welcome!

1. Fork this repository.

2. Create a feature branch.

```bash
git checkout -b feature/NewFeature
```

3. Commit your changes.

```bash
git commit -m "Add New Feature"
```

4. Push the changes.

```bash
git push origin feature/NewFeature
```

5. Open a Pull Request.

---

# 🐞 Reporting Issues

Found a bug or have a feature request?

Please create an issue with a detailed description.

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## **Subham Paul**

Passionate about **Python, Artificial Intelligence, Computer Vision, Automation, Flask, and Web Development.**

- GitHub: https://github.com/subham-paul
- LinkedIn: https://www.linkedin.com/in/subham-paul-india/

---

# ⭐ Show Your Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork the project
- 🤝 Contribute
- 💬 Share your feedback


---

## 🙏 Acknowledgements

Special thanks to the open-source communities behind:

- Python
- Flask
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

for providing the technologies that made this project possible.

---

> **"Present smarter—control your slides with just a wave of your hand."** 🖐️🎤📽️
