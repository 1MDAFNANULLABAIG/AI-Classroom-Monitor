import cv2
import time

from detector import PersonDetector
from posture import PostureAnalyzer
from face_mesh import FaceAnalyzer
from database import save_attendance

# Initialize modules
detector = PersonDetector()
posture = PostureAnalyzer()
face = FaceAnalyzer()

cap = cv2.VideoCapture(0)

# Prevent duplicate attendance every frame
last_saved = {}

while True:
    ret, frame = cap.read()

    if not ret:
        break

    persons = detector.detect(frame)

    cv2.putText(
        frame,
        f"Students : {len(persons)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    current_time = time.time()

    for i, person in enumerate(persons):

        x1, y1, x2, y2 = person["bbox"]

        student = frame[y1:y2, x1:x2]

        if student.size == 0:
            continue

        posture_status = posture.analyze(student)
        face_status = face.analyze(student)

        # Decide final status
        if posture_status == "Sleeping":
            status = "Sleeping"

        elif posture_status == "Slouching":
            status = "Slouching"

        elif face_status == "Looking Down":
            status = "Looking Down"

        else:
            status = "Good"

        student_name = f"Student {i+1}"

        # Save only once every 30 seconds
        if (
            student_name not in last_saved
            or current_time - last_saved[student_name] > 30
        ):
            save_attendance(student_name, status)
            last_saved[student_name] = current_time

        # Select box color
        if status == "Good":
            color = (0, 255, 0)

        elif status == "Looking Down":
            color = (0, 255, 255)

        elif status == "Slouching":
            color = (0, 165, 255)

        else:
            color = (0, 0, 255)

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

        cv2.putText(
            frame,
            f"{student_name}: {status}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2
        )

    cv2.imshow("AI Classroom Monitor", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()