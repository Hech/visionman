import asyncio
import cv2
import mss
import logging
from PIL import Image, ImageGrab
from templates import TEMPLATES


_logger = logging.getLogger(__name__)


class RockmanAI:
    def __init__(self, config):
        _logger.info("Starting RockmanAI...")
        self.set_config(config)

        self.templates = {}
        self.load_templates()

        self.start_screen_capture()

    def set_config(self, config):
        self.running = config["running"]
        self.screen_capture_running["screen_capture_running"]
        self.img = config["img"]
        self.img_gray = config["img_gray"]

    def load_templates(self):
        count = 0
        for t in TEMPLATES:
            count += 1
            self.templates[t] = cv2.imread(t, cv2.IMREAD_GRAYSCALE)
            _logger.info(f"template {count}: {t}")
        _logger.info("Templates loaded.")

    def set_screen_corner(self, top_left: tuple, bottom_right: tuple) -> None:
        self.top_left = top_left
        self.bottom_right = bottom_right

    def start_screen_capture(self):
        _logger.info(f"Screen Capture: {self.top_left}, {self.bottom_right}")
        with mss.mss() as sct:
            while True:
                self.img = sct.grab(
                    {
                        "top": self.top_left[0],
                        "left": self.top_left[1],
                        "width": self.bottom_right[0] - self.top_left[0],
                        "height": self.bottom_right[1] - self.top_left[1],
                    }
                )
                self.img = np.array(self.img, dtype=np.unit8)
                self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGRA2GRAY)

                self.get_templates()

                cv2.imshow("preview", self.img)
                cv2.waitKey(1)

    def get_templates(self):
        match = {}
        for t in TEMPLATES:
            match[t] = cv2.matchTemplate(
                self.img_gray, self.templates[t], cv2.TM_CCOEFF_NORMED
            )

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)

        if max_val >= 0.85:
            self.img = cv2.circle(
                self.img, (max_loc[0] + 10, max_loc[1] + 20), 30, (0, 255, 0), 3, 2
            )
            self.img = cv2.putText(
                self.img,
                t,
                (max_loc[0] + 45, max_loc[1] + 25),
                cv2.FONT_HERSHEY_PLAIN,
                1,
            )


if __name__ == "__main__":
    rockman = RockmanAI(settings.ROCKMAN_SETTINGS)
