import pyautogui
import time

def read_file_and_type(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        pyautogui.write(text, interval=0.05)  # Adjust interval for typing speed

if __name__ == "__main__":
    file_path = "C:\\Users\\Daniel\\Desktop\\New Text Document.txt"
    time.sleep(7)  # Allow time to focus the window
    read_file_and_type(file_path)




