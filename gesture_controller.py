# gesture_controller.py
from gesture import Gesture  # Make sure this import matches the location of your gesture.py file

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
        # Handle other gestures if needed
