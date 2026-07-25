import cv2
import mediapipe as mp
import math


class PostureAnalyzer:

    def __init__(self):

        self.mp_pose = mp.solutions.pose

        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def angle(self, a, b, c):

        angle = math.degrees(
            math.atan2(c[1]-b[1], c[0]-b[0]) -
            math.atan2(a[1]-b[1], a[0]-b[0])
        )

        angle = abs(angle)

        if angle > 180:
            angle = 360-angle

        return angle

    def analyze(self, image):

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        result = self.pose.process(rgb)

        if not result.pose_landmarks:
            return "No Pose"

        lm = result.pose_landmarks.landmark

        nose = lm[self.mp_pose.PoseLandmark.NOSE]

        left_shoulder = lm[self.mp_pose.PoseLandmark.LEFT_SHOULDER]

        left_hip = lm[self.mp_pose.PoseLandmark.LEFT_HIP]

        h, w, _ = image.shape

        n = (nose.x*w, nose.y*h)

        s = (left_shoulder.x*w, left_shoulder.y*h)

        hip = (left_hip.x*w, left_hip.y*h)

        vertical = (s[0], s[1]-100)

        neck_angle = self.angle(vertical, s, n)

        back_angle = self.angle(vertical, s, hip)

        if neck_angle > 35:

            posture = "Sleeping"

        elif neck_angle > 20:

            posture = "Looking Down"

        elif back_angle > 20:

            posture = "Slouching"

        else:

            posture = "Good"

        return posture