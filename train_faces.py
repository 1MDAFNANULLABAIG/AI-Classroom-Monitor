import os
import pickle

dataset = "dataset"
encodings = {}

if not os.path.exists(dataset):
    print("Dataset folder not found.")
    exit()

for student_id in os.listdir(dataset):

    folder = os.path.join(dataset, student_id)

    if not os.path.isdir(folder):
        continue

    images = []

    for file in os.listdir(folder):

        if file.lower().endswith((".jpg", ".jpeg", ".png")):

            images.append(os.path.join(folder, file))

    encodings[student_id] = images

os.makedirs("models", exist_ok=True)

with open("models/student_dataset.pkl", "wb") as f:
    pickle.dump(encodings, f)

print("===================================")
print("Training completed successfully!")
print(f"Students : {len(encodings)}")

for sid in encodings:
    print(f"{sid} -> {len(encodings[sid])} images")

print("Model saved as:")
print("models/student_dataset.pkl")
print("===================================")