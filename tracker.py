import math


class StudentTracker:
    def __init__(self):
        self.students = {}
        self.next_id = 1

    def update(self, detections):
        results = {}

        for det in detections:

            x1, y1, x2, y2 = det["bbox"]

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            assigned = None

            for sid, (px, py) in self.students.items():

                distance = math.sqrt((cx - px) ** 2 + (cy - py) ** 2)

                if distance < 60:
                    assigned = sid
                    break

            if assigned is None:
                assigned = self.next_id
                self.next_id += 1

            self.students[assigned] = (cx, cy)

            results[assigned] = det

        return results