import cv2

# load face detector
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    return faces


def capture_faces(name):
    global running
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    running = True
    count = 0

    while running:
        ret, frame = cam.read()
        if not ret:
            break

        faces = detect_faces(frame)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            face = cv2.resize(face, (100, 100))

            cv2.imwrite(f"static/faces/{name}_{count}.jpg", face)
            count += 1

        cv2.imshow("Capturing...", frame)

        if count >= 5:
            break

        # if cv2.waitKey(1) == 27:
        #     break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()