**M D Afnanullabaig**
# 🎓 AI Classroom Monitor

An AI-powered classroom monitoring system that automates attendance using face recognition and analyzes student behavior in real time. The system detects students, marks attendance automatically, monitors classroom activities, and provides analytics through an interactive Streamlit dashboard.

---

## 📌 Features

- ✅ Student Registration
- 👤 Face Recognition (LBPH)
- 📸 Automatic Face Dataset Collection
- 📝 Automatic Attendance System
- 🧍 Person Detection using YOLOv8
- 😴 Sleeping Detection
- 👀 Looking Down Detection
- 🪑 Slouching Detection
- 📱 Phone Detection
- 📊 Streamlit Analytics Dashboard
- 💾 SQLite Database
- 📈 Attendance & Behaviour Reports

---

## 🛠️ Tech Stack

- Python 3.11
- OpenCV
- YOLOv8
- MediaPipe
- SQLite
- Streamlit
- Pandas
- NumPy
- Tkinter

---

# 📁 Project Structure

```text
AI-Classroom-Monitor/
│
├── backend/
│   ├── app.py
│   ├── dashboard.py
│   ├── database.py
│   ├── register_student.py
│   ├── recognize_student.py
│   ├── train_model.py
│   ├── detector.py
│   ├── posture.py
│   ├── face_mesh.py
│   ├── phone_detector.py
│   ├── tracker.py
│   ├── classroom.db
│   ├── dataset/
│   ├── trainer/
│   └── models/
│
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/1MDAFNANULLABAIG/AI-Classroom-Monitor.git
```

```bash
cd AI-Classroom-Monitor
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate (Windows)

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Commands

### Go to Backend

```bash
cd backend
```

---

### Create Database

```bash
python database.py
```

---

### Register Students

```bash
python register_student.py
```

---

### Train Face Recognition Model

```bash
python train_model.py
```

---

### Test Face Recognition

```bash
python recognize_student.py
```

---

### Start AI Classroom Monitoring

```bash
python app.py
```

---

### Launch Dashboard

```bash
streamlit run dashboard.py
```

Open in browser:

```
http://localhost:8501
```

---

# 📂 Database Tables

### Students

- Student ID
- Student Name
- Department
- Semester
- Section

### Attendance

- Student ID
- Student Name
- Date
- Time
- Status

### Behaviour

- Student ID
- Student Name
- Behaviour
- Date
- Time

---

# 🎯 AI Modules

- Face Recognition
- Person Detection
- Sleeping Detection
- Looking Down Detection
- Slouching Detection
- Phone Detection

---

# 📊 Dashboard

The Streamlit dashboard provides:

- Total Students
- Attendance Summary
- Present Students
- Behaviour Logs
- Charts & Analytics
- Attendance History

---

# 📷 Dataset

Captured face images are stored inside:

```text
backend/dataset/
```

Each student has a separate folder.

Example:

```text
dataset/
├── 1HK23IS001/
├── 1HK23IS002/
├── 1HK23IS003/
```

---

# 🤖 Face Recognition

This project uses:

- Haar Cascade Face Detection
- LBPH Face Recognizer

Generated model:

```text
backend/trainer/trainer.yml
```

---

# 📈 Future Improvements

- FaceNet Recognition
- DeepFace Integration
- Multi-Camera Support
- Cloud Database
- Teacher Login
- Student Portal
- Email Notifications
- Mobile App
- AI Analytics
![alt text](20.jpg)
![alt text](14.jpg)
---

# 👨‍💻 Author

**M D Afnanullabaig**

- Information Science & Engineering
- HKBK College of Engineering
- Bengaluru, Karnataka

---

# 📜 License

This project is developed for educational and research purposes.

---

## ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub and sharing your feedback.

## 🔗 GitHub Repository

**Repository:** https://github.com/1MDAFNANULLABAIG/AI-Classroom-Monitor
