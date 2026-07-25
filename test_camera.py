import cv2
import os

os.makedirs("dataset/test", exist_ok=True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera could not be opened!")
    exit()

print("✅ Camera opened successfully.")
print("Press 'c' to save an image.")
print("Press 'q' to quit.")

count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to read frame.")
        break

    cv2.imshow("Camera Test", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        count += 1
        filename = f"dataset/test/{count}.jpg"

        success = cv2.imwrite(filename, frame)

        if success:
            print(f"✅ Saved: {filename}")
        else:
            print(f"❌ Failed to save: {filename}")

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()