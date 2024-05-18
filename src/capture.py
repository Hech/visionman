import mss
import pyautogui
import numpy as np
import cv2
import time
import multiprocessing
import settings

class CaptureAgent:
    def __init__(self)->None:
        self.capture_proc = None
        self.fps = None
        self.preview_enabled = True
        
        self.width, self.height = pyautogui.size()
        print(f"Screensize: {self.width}x{self.height}")

        self.monitor = {
            'top': settings.MONITOR_TOP_LEFT[1],
            'left': settings.MONITOR_TOP_LEFT[0],
            'width': settings.MONITOR_BOTTOM_RIGHT[0],
            'height': settings.MONITOR_BOTTOM_RIGHT[1]
        }

if __name__ == "__main__":
    agent = CaptureAgent()
