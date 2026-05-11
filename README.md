# 🖐️ AI Air Canvas

### Draw in the air. No touch required.

A real-time touchless drawing interface built with Python, OpenCV, and MediaPipe. Using just a webcam and your hand, you can draw, sketch, and interact with a digital canvas — no mouse, no stylus, no physical contact needed.

---

## 🎯 Project Overview

AI Air Canvas uses computer vision to track hand movements in real time and translates them into drawing actions on a digital canvas. The system detects 21 hand landmarks per frame, identifies finger gestures, and maps their positions to canvas coordinates — all at live video speed.

This project was built as a Final Year Project at Tirumala Engineering College, led by a team of 4 using Agile development principles.

---

## ✨ Features

- 🖐️ Real-time 21-point hand landmark detection
- ✏️ Touchless drawing using index finger tracking
- 🎨 Multiple color selection via gesture
- 🗑️ Air erase functionality
- 📷 Live webcam feed with canvas overlay
- ⚡ High-precision gesture recognition (~85% accuracy)

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Computer Vision | OpenCV |
| Hand Tracking | MediaPipe |
| Gesture Recognition | Custom landmark logic |
| IDE | VS Code / Google Colab |

---

## 📁 Project Structure

```
Air-Canvas/
│
├── main.py              # Main application entry point
├── main_new.py          # Updated version with improved gesture logic
├── HandTrack.py         # Hand tracking module using MediaPipe
├── cam.py               # Camera feed handler
├── mp_test.py           # MediaPipe testing and calibration
├── run.bat              # Windows run script
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.x installed. Then install the required libraries:

```bash
pip install opencv-python mediapipe numpy
```

### Run the Application

```bash
python main.py
```

Or on Windows, simply double-click `run.bat`

### How to Use

1. Run the application — your webcam will activate
2. Hold your hand in front of the camera
3. **Index finger up** → Drawing mode
4. **Index + Middle finger up** → Selection mode (choose colors)
5. **All fingers up** → Erase mode
6. Move your hand to draw on the canvas

---

## 🧠 How It Works

```
Webcam Feed
     ↓
MediaPipe Hand Detection
     ↓
21 Landmark Points Extracted
     ↓
Finger State Analysis (up/down)
     ↓
Gesture Classification
     ↓
Canvas Drawing / Color Selection / Erase
     ↓
Real-time OpenCV Display
```

1. **Hand Detection** — MediaPipe processes each frame and returns 21 3D landmark coordinates for the detected hand
2. **Gesture Recognition** — Finger tip and base landmark positions are compared to determine which fingers are raised
3. **Drawing Logic** — Index finger tip coordinates are mapped to the canvas and connected frame-by-frame to create smooth strokes
4. **Canvas Overlay** — The drawing canvas is blended with the live webcam feed using OpenCV for a seamless AR effect

---

## 📊 Results

- ✅ 85% gesture recognition accuracy during testing
- ✅ Functional prototype demonstrated to faculty panel
- ✅ 30% improvement in interactive learning engagement vs traditional input methods
- ✅ Real-time performance at standard webcam frame rates

---

## 👥 Team

| Role | Name |
|---|---|
| Team Lead & Developer | Julakanti Sai Akshaya |
| Developer | Team Member 2 |
| Developer | Team Member 3 |
| Developer | Team Member 4 |

*Final Year Project — Tirumala Engineering College, BTech CSE (2022–2026)*

---

## 📜 Certifications & Background

- Python Programming — NPTEL Certified
- Infosys Pragati: Path to Future — Cohort 5
- Completed be10X AI Tools Workshop

---

## 📬 Connect

**Julakanti Sai Akshaya**
- 🔗 [LinkedIn](https://www.linkedin.com/in/julakanti-sai-akshaya)
- 📧 julakantiakshaya300@gmail.com
- 💻 [GitHub](https://github.com/SaiAkshaya18)

---

⭐ *If you found this project interesting, consider giving it a star!*


https://resume-ranker-pro.streamlit.app
