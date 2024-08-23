import cv2
import numpy as np
from gesture import Gesture
import hagrid

class BasicHandDetector:
    def __init__(self):
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=25, detectShadows=True)

    def detect_movement(self, frame):
        fg_mask = self.bg_subtractor.apply(frame)
        _, thresh = cv2.threshold(fg_mask, 25, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def classify_movement(self, contours, frame):
        for contour in contours:
            if cv2.contourArea(contour) > 5000:
                x, y, w, h = cv2.boundingRect(contour)
                aspect_ratio = w / float(h)
                if aspect_ratio > 1.2:
                    if x < frame.shape[1] // 3:
                        return Gesture.LEFT_SWIPE
                    elif x > frame.shape[1] * 2 // 3:
                        return Gesture.RIGHT_SWIPE
                else:
                    if y < frame.shape[0] // 3:
                        return Gesture.FINGER_UP
                    elif y > frame.shape[0] * 2 // 3:
                        return Gesture.FINGER_DOWN
        return None

class HagridHandDetector:
    def __init__(self):
        self.hagrid_detector = hagrid.HandDetector()

    def detect_fingers(self, frame):
        return self.hagrid_detector.detect(frame)  # Assuming detect method provides finger count

class HandDetector:
    def __init__(self, gesture_model):
        self.basic_detector = BasicHandDetector()
        self.hagrid_detector = None  # Default to None
        try:
            self.hagrid_detector = HagridHandDetector()
        except Exception as e:
            print(f"Warning: HagridHandDetector could not be initialized: {e}")
        self.gesture_model = gesture_model

    def detect_hand(self, frame):
        contours = self.basic_detector.detect_movement(frame)
        gesture = self.basic_detector.classify_movement(contours, frame)
        
        if gesture is None and self.hagrid_detector:
            finger_count = self.hagrid_detector.detect_fingers(frame)
            gesture = self.map_finger_count_to_gesture(finger_count)
            
        return gesture

    def preprocess_for_nn(self, frame):
        resized = cv2.resize(frame, (224, 224))  # Adjusted for MobileNetV2
        normalized = resized / 255.0
        return np.expand_dims(normalized, axis=0)

    def classify_with_nn(self, hand_img):
        predictions = self.gesture_model.predict(hand_img)
        gesture_idx = np.argmax(predictions)
        return Gesture(gesture_idx + 1)

    def map_finger_count_to_gesture(self, finger_count):
        if finger_count == 1:
            return Gesture.OPEN_HAND  # Playing a song
        elif finger_count == 2:
            return Gesture.CLOSED_FIST  # Pausing the song
        elif finger_count == 3:
            return Gesture.FINGER_UP  # Raising the volume
        elif finger_count == 4:
            return Gesture.FINGER_DOWN  # Lowering the volume
        elif finger_count == 5:
            return Gesture.RIGHT_SWIPE  # Next media
        else:
            return None
