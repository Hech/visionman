import asyncio
import cv2
import logging

from templates import TEMPLATES


_logger = logging.getLogger(__name__)
class RockmanAI:
    def __init__(self, settings):
        self.settings = settings
        _logger.info("Starting RockmanAI...")
        print("Loading templates...")

        self.templates = {}
        count = 0
        for t in TEMPLATES:
            count += 1
            self.templates[t] = cv2.imread(TEMPLATES[t], cv2.IMREAD_GRAYSCALE)
            print(f"template {count}: {t}")

    async def setup_templates(self):
        count = 0
        for t in TEMPLATES:
            try:
                await self.load_templates

    def set_screen_corner(self, top_left: tuple, bottom_right:tuple)->None:
        self.top_left = top_left
        self.bottom_right = bottom_right

    def start_screen_capture(self):
        print(f"Screen Capture: {self.top_left}, {self.bottom_right}")


if __name__ == "__main__":
    rockman = RockmanAI(settings.ROCKMAN_SETTINGS)
