Squat Counter Using OpenCV and MediaPipe

A real-time squat counter built with Python, OpenCV, and MediaPipe Pose. The application uses webcam input to detect body landmarks, calculate the knee angle, track squat movements, and count completed repetitions.

✨ Features

- Real-Time Pose Detection: Detects body landmarks using MediaPipe Pose.
- Knee Angle Calculation: Calculates the angle between the hip, knee, and ankle.
- Automatic Squat Counting: Counts a repetition when the user bends and then straightens their knee.
- Movement Tracking: Displays the current stage of the squat ("up" or "down").
- Live Webcam Display: Shows the camera feed with the current stage and repetition count.

🛠️ Technologies

- Python
- OpenCV
- MediaPipe
- Math (Python standard library)

⚙️ Installation

Make sure Python is installed on your system.

Install the required libraries:

pip install opencv-python mediapipe

▶️ Usage

1. Save the Python code in a file named "squat_counter.py".
2. Make sure your webcam is connected and available.
3. Run the application:

python squat_counter.py

4. Stand where your hip, knee, and ankle can be detected by the webcam.
5. Perform squats and watch the repetition counter update in real time.
6. Press "q" to exit the application.

🧠 How It Works

1. Pose Detection

MediaPipe Pose detects body landmarks from each webcam frame. The application uses the following landmarks from the detected pose:

- Hip: Landmark 24
- Knee: Landmark 26
- Ankle: Landmark 28

These landmark indices correspond to the right leg in MediaPipe Pose.

2. Knee Angle Calculation

The "angle_calculator()" function calculates the angle formed by three points:

angle = angle_calculator(hip, knee, ankle)

The knee serves as the vertex of the angle.

3. Squat Stage Detection

The application uses two angle thresholds to determine the current movement stage:

- Down: The knee angle falls below 140 degrees.
- Up: The knee angle exceeds 160 degrees after the movement has reached the "down" stage.

When the user transitions from "down" to "up", the repetition counter increases by one.

Using separate thresholds helps prevent repeated counting from small angle fluctuations around a single threshold.

📁 Project Structure

squat-counter/
├── squat_counter.py
└── README.md

⚠️ Limitations

- The application requires a working webcam.
- Accurate detection depends on camera placement, lighting, and body visibility.
- The current implementation tracks only one leg.
- The angle thresholds are fixed and may not work equally well for every user or camera position.
- The program counts repetitions based on knee angle changes; it does not evaluate overall squat form or guarantee correct exercise technique.

🚀 Possible Improvements

- Display pose landmarks and the knee angle on the video.
- Support left-leg and right-leg tracking.
- Add configurable angle thresholds.
- Improve detection stability using landmark visibility checks and angle smoothing.
- Track workout duration and save repetition statistics.
- Add support for other exercises, such as push-ups and bicep curls.

📄 License

This project is intended for educational and personal use.
