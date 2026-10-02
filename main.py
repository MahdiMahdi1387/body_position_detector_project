import cv2
import mediapipe as mp
import math


def angle_calculator(a: tuple, b: tuple, c: tuple) -> float:
    radian = math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0])
    degree = abs(math.degrees(radian))
    return 360 - degree if degree > 180 else degree


cap = cv2.VideoCapture(0)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

count = 0
stage = 'up'

while True:
    success, frame = cap.read()

    if not success:
        break

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(frameRGB)

    if result.pose_landmarks:
        landmarks = result.pose_landmarks.landmark

        hip = (landmarks[24].x, landmarks[24].y)
        knee = (landmarks[26].x, landmarks[26].y)
        ankle = (landmarks[28].x, landmarks[28].y)

        angle = angle_calculator(hip, knee, ankle)

        if angle < 140:
            stage = 'down'
        if angle > 160 and stage == 'down':
            stage = 'up'
            count += 1

        cv2.putText(frame, f'Stage: {stage}', (20, 40),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f'Count: {count}', (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        

    cv2.imshow('Webcam', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
