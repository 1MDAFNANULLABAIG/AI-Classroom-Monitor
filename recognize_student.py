import cv2
import os
from database import mark_attendance

# -----------------------------
# Load LBPH Model
# -----------------------------
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")

# -----------------------------
# Load Labels
# -----------------------------
labels = {}

with open("trainer/labels.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            label, student_id = line.split(",")
            labels[int(label)] = student_id

# -----------------------------
# Load Haar Cascade
# -----------------------------
cascade_path = "models/haarcascade_frontalface_default.xml"

if not os.path.exists(cascade_path):
    print("ERROR: Haar Cascade XML not found!")
    exit()

face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print("ERROR: Failed to load Haar Cascade.")
    exit()

# -----------------------------
# Camera
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

print("===================================")
print(" AI Classroom Face Recognition")
print(" Press Q to Exit")
print("===================================")

attendance_done = set()

# Change this if recognition is too strict/loose
THRESHOLD = 55

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        label, confidence = recognizer.predict(face)

        print(f"Label={label}  Confidence={confidence:.2f}")

        if confidence < THRESHOLD:

            student_id = labels.get(label, "Unknown")

            color = (0, 255, 0)
            text = student_id

            # Mark attendance only once
            if student_id not in attendance_done:
                mark_attendance(student_id)
                attendance_done.add(student_id)
                print(f"Attendance Marked -> {student_id}")

        else:

            text = "Unknown"
            color = (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

        cv2.putText(
            frame,
            text,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

        cv2.putText(
            frame,
            f"Confidence: {confidence:.1f}",
            (x, y+h+25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )

    cv2.imshow("AI Classroom Monitoring", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("Program Closed")