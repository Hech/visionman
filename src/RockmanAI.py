import asyncio
import cv2
import mss
import logging

from templates import TEMPLATES


_logger = logging.getLogger(__name__)
class RockmanAI:
    def __init__(self, settings):
        self.settings = settings
        _logger.info("Starting RockmanAI...")
        self.run_with_config()

        self.templates = {}
        self.load_templates()

    def load_templates(self):
        count = 0
        for t in TEMPLATES:
            count += 1
            self.templates[t] = cv2.imread(TEMPLATES[t], cv2.IMREAD_GRAYSCALE)
            _logger.info(f"template {count}: ")
        _logger.info("Templates loaded.")

    def set_screen_corner(self, top_left: tuple, bottom_right:tuple)->None:
        self.top_left = top_left
        self.bottom_right = bottom_right

    def start_screen_capture(self):
        _logger.info(f"Screen Capture: {self.top_left}, {self.bottom_right}")
        with mss.mss() as sct:
            while True:
                self.img = sct.grab("top": self.top_left[0], "left": self.top_left[1], "width": self.bottom_right[0] - self.top_left[0])
                self.img = np.array(self.img, dtype=np.unit8)
                self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGRA2GRAY)

                self.get_templates()

                cv2.imshow("preview", self.img)
                cv2.waitKey(1)

    def get_templates(self):
        matches = {}
        for t in templates.keys():
            match[t] = cv2.match(self.img_gray, self.templates[t], cv2.TM_COEFF_NORMED])
        

if __name__ == "__main__":
    rockman = RockmanAI(settings.ROCKMAN_SETTINGS)
