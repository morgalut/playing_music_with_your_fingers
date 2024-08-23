import os
import random
import threading
import cv2
from pygame import mixer
from gesture import VolumeControl, Gesture

class MediaController:
    def __init__(self, media_folder):
        self.media_folder = media_folder
        self.playlist = self.load_playlist()
        self.current_media_index = -1
        mixer.init()
        self.video_thread = None
        self.video_running = False
        self.is_playing = False

    def load_playlist(self):
        supported_formats = ('.mp3', '.mp4')
        playlist = [os.path.join(self.media_folder, f) for f in os.listdir(self.media_folder) if f.endswith(supported_formats)]
        if not playlist:
            raise ValueError("No media files found in the specified folder.")
        random.shuffle(playlist)
        return playlist

    def refresh_playlist(self):
        self.playlist = self.load_playlist()

    def play_media(self):
        if not self.is_playing:
            self.stop_media()
            self.current_media_index = (self.current_media_index + 1) % len(self.playlist)
            current_file = self.playlist[self.current_media_index]
            if current_file.endswith('.mp3'):
                mixer.music.load(current_file)
                mixer.music.play()
            elif current_file.endswith('.mp4'):
                self.play_video(current_file)
            self.is_playing = True

    def stop_media(self):
        if self.is_playing:
            mixer.music.stop()
            self.is_playing = False
            if self.video_thread:
                self.video_thread.join()

    def play_video(self, video_path):
        if self.video_thread and self.video_running:
            return

        self.video_running = True
        self.video_thread = threading.Thread(target=self._play_video, args=(video_path,))
        self.video_thread.start()

    def _play_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        while self.video_running and cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Video', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def control_volume(self, direction):
        volume = mixer.music.get_volume()
        if direction == VolumeControl.UP:
            mixer.music.set_volume(min(1.0, volume + 0.1))
        elif direction == VolumeControl.DOWN:
            mixer.music.set_volume(max(0.0, volume - 0.1))

    def handle_gesture(self, gesture):
        if gesture == Gesture.RIGHT_SWIPE:
            print("Next media")
            self.play_media()
        elif gesture == Gesture.LEFT_SWIPE:
            print("Previous media")
            self.current_media_index = (self.current_media_index - 2) % len(self.playlist)
            self.play_media()
        elif gesture == Gesture.FINGER_UP:
            self.control_volume(VolumeControl.UP)
        elif gesture == Gesture.FINGER_DOWN:
            self.control_volume(VolumeControl.DOWN)
        elif gesture == Gesture.OPEN_HAND:
            self.play_media()
        elif gesture == Gesture.CLOSED_FIST:
            self.stop_media()
