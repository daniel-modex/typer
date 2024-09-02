import pyautogui
import time
import pygame
import tkinter as tk
import threading

# Global variable to control sound playback
stop_sound = False

def read_file_and_type(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        pyautogui.write(text, interval=0.05)  # Adjust interval for typing speed


def play_sound(sound_path):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Loop to keep the sound playing
        if stop_sound:  # Check if stop signal was given
            pygame.mixer.music.stop()
            break
        pygame.time.Clock().tick(10)


def show_popup():
    global stop_sound
    # Create the main window
    root = tk.Tk()
    root.title("Notification")

    # Add a label
    label = tk.Label(root, text="Text typing completed!")
    label.pack(pady=10)

    # Add a button to stop the sound
    def stop_button_clicked():
        global stop_sound
        stop_sound = True
        root.destroy()  # Close the popup window

    stop_button = tk.Button(root, text="Stop Sound", command=stop_button_clicked)
    stop_button.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    file_path = "text.txt"
    sound_path = "digital-alarm-clock-151920.mp3"
    time.sleep(7)  # Allow time to focus the window
    read_file_and_type(file_path)
     # Start the sound in a separate thread
    sound_thread = threading.Thread(target=play_sound, args=(sound_path,))
    sound_thread.start()
    
    # Show the popup window
    show_popup()
    
    # Wait for the sound thread to finish before exiting
    sound_thread.join()
    




