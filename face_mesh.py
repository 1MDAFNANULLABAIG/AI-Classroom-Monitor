import cv2
import mediapipe as mp


class FaceAnalyzer:

    def __init__(self):
        self.mp_face = mp.solutions.face_mesh

        self.face_mesh = self.mp_face.FaceMesh(
            max_num_faces=5,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def analyze(self, image):

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        result = self.face_mesh.process(rgb)

        if not result.multi_face_landmarks:
            return "No Face"

        h, w, _ = image.shape

        for face in result.multi_face_landmarks:

            left_eye = face.landmark[159]
            right_eye = face.landmark[386]

            left_eye_y = left_eye.y
            right_eye_y = right_eye.y

            eye_level = (left_eye_y + right_eye_y) / 2

            if eye_level > 0.45:
                return "Looking Down"

            return "Awake"

        return "No Face"