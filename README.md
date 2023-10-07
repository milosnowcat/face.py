# face.py
 Face Detection

## Installation of the Face.py Project

This project allows you to capture video from a webcam, detect faces, and recognize and label them. To get started with this project, follow the installation steps below.

### Prerequisites

Before using the project, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. Clone the GitHub repository containing the Face.py project to your local machine using the following command:

   ```bash
   git clone https://github.com/milosnowcat/face.py.git
   ```

2. Navigate to the `face.py` directory:

   ```bash
   cd face.py
   ```

3. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the `main.py` script to start the face detection and recognition:

   ```bash
   python main.py
   ```

5. The script will use your webcam to capture video and perform real-time face detection and recognition.

6. Recognized faces will be labeled, and their names will be displayed on the video stream.

7. To exit the application, press the `Esc` key (usually represented as `k == 27` in the terminal).

That's it! You have successfully installed and used the Face.py project for real-time face detection and recognition.

---

## Using the Face.py Project

The Face.py project enables real-time face detection and recognition using your webcam. Follow these steps to use the project.

### Face Detection and Recognition

1. Ensure you have followed the installation steps mentioned in the "Installation of the Face.py Project" section.

2. Run the `main.py` script to start the face detection and recognition:

   ```bash
   python main.py
   ```

3. The script will capture video from your webcam and display it in a window.

4. Faces detected in the video stream will be outlined, and their names (if recognized) will be displayed below each detected face.

5. The recognition is based on known faces extracted from the `assets/images` directory and encoded using face_recognition.

6. To exit the application, press the `Esc` key (usually represented as `k == 27` in the terminal).

7. If you want to add new faces for recognition, you can place images containing the faces in the `assets/images` directory and run the `extractFaces` function provided in the `utils.py` script.

That's it! You have successfully used the Face.py project for real-time face detection and recognition using your webcam.
