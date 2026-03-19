from flask import Flask, render_template, request, redirect
import cv2
import pandas as pd
import datetime

from utils import detect_faces, capture_faces
from train_model import train_model

app = Flask(__name__)

model = None   # train only after reg
running = False
last_marked = {}
def mark_attendance(name):
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%Y-%m-%d")
    if name in last_marked:
        diff = (now - last_marked[name]).seconds
        if diff < 20:
            return
    last_marked[name]=now
    try:
        df = pd.read_csv("attendance.csv")
    except:
        df = pd.DataFrame(columns=["Name", "Date", "Time"])

    
    new = pd.DataFrame([[name, date_str,  time_str]], columns=["Name", "Date", "Time"])
    df = pd.concat([df, new], ignore_index=True)
    df.to_csv("attendance.csv", index=False)
    print("Marked:",name)

def start_camera():
    global model

    if model is None:
        print("No users registered!")
        return

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while running:
        ret, frame = cam.read()
        if not ret:
            break

        faces = detect_faces(frame)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]

            gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            gray = cv2.resize(gray, (100, 100)).flatten().reshape(1, -1)
            try:
                name = model.predict(gray)[0]
                mark_attendance(name)
            except:
                name = "Unknown"
            

            cv2.putText(frame, name, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        cv2.imshow("Attendance", frame)

        if cv2.waitKey(1) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()


@app.route("/")
def home():
    return render_template("index.html")


# registration
@app.route("/register", methods=["POST"])
def register():
    global model

    name = request.form.get("name")

    if name:
        capture_faces(name)   # open camera  capture
        model = train_model() # retrain after adding new user
        if model is None:
            print("Training failed - no images found")
    return redirect("/")


# start of attendance
@app.route("/start")
def start():
    global running
    running = True
    start_camera()
    print("Started")
@app.route("/stop")
def stop():
    global running
    running = False
    print("Stopped")

@app.route("/attendance")
def attendance():
    try:
        df = pd.read_csv("attendance.csv")
    except:
        df = pd.DataFrame(columns=["Name", "Date", "Time"])

    data = df.to_dict(orient="records")
    return render_template("attendance.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)