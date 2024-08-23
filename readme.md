

# Gesture-Based Media Controller

## Overview

The Gesture-Based Media Controller is a Python application that enables control of media playback using hand gestures. By detecting gestures such as "FINGER_UP" and "FINGER_DOWN," the application can play or stop media, making it an intuitive and hands-free way to interact with media.

## Features

- **Gesture Detection**: Detects specific hand gestures using a hand detection algorithm.
- **Media Control**: Controls media playback based on detected gestures.
- **Modular Design**: Separate modules for hand detection and media control.

## Prerequisites

Before you start, ensure you have the following installed:

- Python 3.7 or later
- Required Python libraries (see Installation section)
- A hand detection library compatible with your setup

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/morgalut/gesture-based-media-controller.git
   cd gesture-based-media-controller
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Required Libraries**

   Install the required libraries using `pip`. Ensure that you have a `requirements.txt` file in the root of your project.

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

1. **Prepare Your Hand Detection Model**

   Ensure that your hand detection model is set up and accessible by the application.

2. **Configure the Application**

   Update the configuration settings in `config.py` or any other configuration file to suit your needs.

3. **Start the Application**

   Run the main script to start the application:

   ```bash
   python main.py
   ```

### Code Overview

- `gesture.py`: Defines the `Gesture` enumeration which represents different hand gestures.

  ```python
  from enum import Enum

  class Gesture(Enum):
      FINGER_UP = 1
      FINGER_DOWN = 2
      # Add more gesture types as needed
  ```

- `gesture_controller.py`: Contains the `GestureController` class which handles gesture detection and media control.

  ```python
  from gesture import Gesture

  class GestureController:
      def __init__(self, hand_detector, media_controller):
          self.hand_detector = hand_detector
          self.media_controller = media_controller

      def process_frame(self, frame):
          gesture = self.hand_detector.detect_hand(frame)
          if gesture:
              self.handle_gesture(gesture)

      def handle_gesture(self, gesture):
          if gesture == Gesture.FINGER_UP:
              self.media_controller.play_media()
          elif gesture == Gesture.FINGER_DOWN:
              self.media_controller.stop_media()
  ```

- `hand_detector.py`: Implements the `HandDetector` class for detecting hand gestures.

- `media_controller.py`: Manages media playback operations such as play and stop.

## Contributing

We welcome contributions to improve the Gesture-Based Media Controller. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your branch.
4. Create a pull request with a description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact:

- **Email**: [morgalut54@gmail.com](mailto:morgalut54@gmail.com)
- **GitHub**: [https://github.com/morgalut](https://github.com/morgalut)

