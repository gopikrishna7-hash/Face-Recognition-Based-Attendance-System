# Face Based Attendance System

This project is a simple and practical face recognition-based attendance system built using Python, Flask, and OpenCV.

It allows users to register their face and automatically mark attendance using a webcam.

---

## 🚀 Features

- Register new users using face capture
- Real-time face detection using Haar Cascade
- Face recognition using KNN algorithm
- Automatic attendance marking with date and time
- View attendance records in a web interface
- Clean and simple dashboard UI

---

## 🛠️ Technologies Used

- Python
- Flask
- OpenCV
- Haar Cascade Algorithm
- KNN (K-Nearest Neighbors)
- HTML, CSS
- Pandas

---

## 📁 Project Structure
Face-Attendance/
│
├── app.py # Main Flask application
├── utils.py # Face detection and capture functions
├── train_model.py # Model training (KNN)
├── attendance.csv # Attendance records
├── haarcascade_frontalface_default.xml
│
├── templates/
│ ├── index.html # Dashboard
│ └── attendance.html # Attendance display
│
├── static/
│ ├── css/
│ │ └── style.css # UI styling
│ └── faces/ # Stored face images

---

## ⚙️ How It Works

1. User enters name and registers
2. System captures multiple face images using webcam
3. Images are stored in `static/faces/`
4. Model is trained using KNN algorithm
5. When attendance starts:
   - Face is detected using Haar Cascade
   - Recognized using trained model
   - Attendance is marked in CSV file

---

## ▶️ How to Run
### 1. Install dependencies
### 2. Run the application python app.py
### 3. Open browser

---

## 🧾 Usage

### 🔹 Register User
- Enter name in input box
- Click "Register"
- Camera will capture face images

---

### 🔹 Start Attendance
- Click "Start"
- System will detect and recognize face
- Attendance is recorded automatically

---

### 🔹 View Attendance
- Click "View Attendance"
- Displays attendance table

## 📊 Attendance Format
Name, 2026-03-19, 10:30:15
## 🎯 Conclusion

This project demonstrates how computer vision can be used in real-world applications like attendance systems.

It combines face detection and machine learning with a web interface to create a complete working solution.
