import cv2
import os
import numpy as np

DATASET = "dataset"
TRAINER = "trainer"
CASCADE = "models/haarcascade_frontalface_default.xml"

os.makedirs(TRAINER, exist_ok=True)

face_detector = cv2.CascadeClassifier(CASCADE)

if face_detector.empty():
    print("Cannot load Haar Cascade XML.")
    exit()

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []
label_map = {}
label_id = 0

for student in os.listdir(DATASET):

    folder = os.path.join(DATASET, student)

    if not os.path.isdir(folder):
        continue

    label_map[label_id] = student

    for img_name in os.listdir(folder):

        img_path = os.path.join(folder, img_name)

        img = cv2.imread(img_path)

        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        detected = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5
        )

        for (x, y, w, h) in detected:

            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (200, 200))

            faces.append(face)
            labels.append(label_id)

    label_id += 1

if len(faces) == 0:
    print("No faces found in dataset.")
    exit()

recognizer.train(faces, np.array(labels))
recognizer.save(os.path.join(TRAINER, "trainer.yml"))

with open(os.path.join(TRAINER, "labels.txt"), "w") as f:
    for key, value in label_map.items():
        f.write(f"{key},{value}\n")

print("===================================")
print("Training Complete")
print("Faces:", len(faces))
print("Students:", len(label_map))
print("===================================")