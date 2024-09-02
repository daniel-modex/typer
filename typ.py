import pyautogui
import time
import pygame

def read_file_and_type(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        pyautogui.write(text, interval=0.05)  # Adjust interval for typing speed


def play_sound(sound_path):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Wait for the sound to finish playing
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    file_path = "text.txt"
    sound_path = "digital-alarm-clock-151920.mp3"
    time.sleep(7)  # Allow time to focus the window
    read_file_and_type(file_path)
    play_sound(sound_path)




