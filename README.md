🖐️ Gesture-Controlled Slide Presentation (GestureSlides AI)

A touchless presentation control system powered by Computer Vision and Artificial Intelligence.
Control your slides using simple hand gestures — no keyboard, no mouse, no remote.

🚀 Project Overview

GestureSlides AI allows presenters to navigate presentation slides using hand swipe gestures captured through a webcam.
The system detects gestures in real time using MediaPipe Hands, processes motion using OpenCV, and triggers slide navigation using keyboard automation.

This project demonstrates the practical use of AI + Computer Vision + Web Technologies in real-world applications.

✨ Key Features

🖐️ Gesture-Based Control

Swipe Right → Next Slide

Swipe Left → Previous Slide

🎥 Live Camera Feed

Real-time hand tracking with visual feedback

🧠 AI-Powered Vision

MediaPipe Hands for accurate landmark detection

🌐 Web-Based Interface

Flask backend with responsive Bootstrap UI

🖥 Universal Compatibility

Works with PowerPoint, Google Slides, PDF viewers, and browsers

🎓 Viva & Portfolio Ready

Clean architecture, documented, and professional UI

🛠 Tech Stack
Category	Technologies
Backend	Python, Flask
Computer Vision	OpenCV, MediaPipe
Gesture Logic	MediaPipe Hands
Automation	PyAutoGUI
Frontend	HTML, CSS, Bootstrap
Scripting	JavaScript
Streaming	Flask MJPEG video feed
📂 Project Structure
Gesture-Controlled-Slide-Presentation/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   └── js/
│       └── main.js
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   ├── about.html
│   └── contact.html
│
└── venv/

⚙️ How It Works

Camera Capture

Webcam captures live video frames.

Hand Detection

MediaPipe detects hand landmarks in real time.

Gesture Analysis

Wrist X-axis movement is tracked.

Swipe direction is identified.

Action Trigger

Right swipe → Right Arrow key

Left swipe → Left Arrow key

Slide Navigation

Presentation responds instantly.

🧪 Gesture Mapping
Gesture	Action
Swipe Right	Next Slide
Swipe Left	Previous Slide
No Motion	Idle
▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/Gesture-Controlled-Slide-Presentation.git
cd Gesture-Controlled-Slide-Presentation

2️⃣ Create Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000

🧠 Viva Explanation (Short)

“This project uses MediaPipe Hands to detect hand landmarks in real time.
By tracking wrist movement along the X-axis, the system identifies swipe gestures.
These gestures are converted into keyboard events using PyAutoGUI, enabling touchless slide navigation through a Flask web interface.”

🎯 Use Cases

🎓 Classrooms & Smart Boards

🧑‍🏫 Online Teaching

🏢 Corporate Presentations

🎤 Seminars & Conferences

🖥 Accessibility-Focused Interfaces

🔮 Future Enhancements

✋ Add more gestures (pause, zoom, laser pointer)

🎙 Voice + Gesture hybrid control

📱 Mobile camera support

🤖 AI gesture customization

🌍 Cloud deployment

👨‍💻 Developer

Sabuj Dhali
📍 India
🎓 B.Sc Data Science
💡 Interests: AI, Computer Vision, Full-Stack Development

📜 License

This project is for educational and academic purposes.
Feel free to fork, modify, and learn from it."# Gesture_Controlled_Slide_Presentation" 
