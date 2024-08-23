import cv2
from gesture import Gesture
from gesture_model import create_gesture_model
from hand_detector import HandDetector
from media_controller import MediaController
from gesture_controller import GestureController

def main():
    input_shape = (224, 224, 3)  # Adjust based on MobileNetV2 input
    gesture_model = create_gesture_model(input_shape)
    hand_detector = HandDetector(gesture_model)
    media_controller = MediaController(media_folder=r"C:\Users\Mor\Desktop\music")
    gesture_controller = GestureController(hand_detector, media_controller)

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gesture_controller.process_frame(frame)

        cv2.imshow('Hand Gesture Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
