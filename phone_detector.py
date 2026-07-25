from ultralytics import YOLO


class PhoneDetector:

    def __init__(self):

        # COCO model
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):

        results = self.model(frame, verbose=False)

        phones = []

        for box in results[0].boxes:

            cls = int(box.cls[0])

            # COCO class 67 = Cell Phone
            if cls == 67:

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                phones.append((x1, y1, x2, y2))

        return phones