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
        self.img = None
        
        self.width, self.height = pyautogui.size()
        print(f"Screensize: {self.width}x{self.height}")

        self.monitor = {
            'top': settings.MONITOR_TOP_LEFT[1],
            'left': settings.MONITOR_TOP_LEFT[0],
            'width': settings.MONITOR_BOTTOM_RIGHT[0],
            'height': settings.MONITOR_BOTTOM_RIGHT[1]
        }
    def screen_capture(self):
        with mss.mss() as sct:
            while True:
                self.img = sct.grab(self.monitor)
                self.img = np.array(self.img)
                if settings.ENABLE_PREVIEW:
                    preview = cv2.resize(self.img, (0, 0), fx=0.5, fy=0.5)
                    cv2.imshow('Vision', preview)
                    key = cv2.waitKey(1)
                    if key == ord('q'):
                        break
        cv2.destroyAllWindows()

if __name__ == "__main__":
    agent = CaptureAgent()

    agent.screen_capture()
