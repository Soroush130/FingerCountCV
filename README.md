# FingerCountCV

FingerCountCV is a real-time computer vision project that detects and counts the number of fingers raised by a hand. Using OpenCV and MediaPipe, it tracks hand landmarks, analyzes finger positions, and displays the count on the screen. Ideal for gesture-based control and human-computer interaction.

## Features

. Real-time hand and finger tracking.
. Counts and displays the number of raised fingers.
. Utilizes OpenCV and MediaPipe for accurate hand landmark detection.

## How It Works

1. The project uses MediaPipe to detect hand landmarks, such as joints and fingertips.
2. Based on the position of key landmarks, the program counts how many fingers are raised.
3. The count is displayed on the screen in real-time using OpenCV.

## Requirements

Follow these steps to set up the project:

1. Clone the repository :

```bash
git clone https://github.com/Soroush130/FingerCountCV.git
```

```bash
cd FingerCountCV
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

+ On Windows :
```bash
venv/Scripts/activate
```

+ On macOS/Linux :
```bash
source venv/bin/activate
```

4. Install required libraries:

```bash
pip install opencv-python mediapipe pycaw comtypes
```

## Usage
To run the project, make sure your webcam is connected, and then run the following command:

```bash
python main.py
```

The program will launch a webcam window that detects the number of raised fingers in real-time and displays the count on the screen.

## Contributing

Feel free to submit issues or pull requests to improve the project. Contributions are welcome!

## Contact

For any questions, you can reach out via soroosh1381amir@gmail.com
