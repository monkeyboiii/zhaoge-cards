import os
import unittest
import xmlrunner
import base64
import cv2
from time import sleep

from BitBarAppiumTest import BitBarAppiumTest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

from misc import log, _create_dir_if_not_exist


_image_dir = os.environ.get("IMAGE_RECOGNITION_DIR") or 'images'
IMAGE_REFRESH_RATE = int(os.environ.get("IMAGE_REFRESH_RATE") or 10)
IMAGE_OCCURRENCE_THRESHOLD = float(
    os.environ.get("IMAGE_OCCURRENCE_THRESHOLD") or 0.5)
IMAGE_SIMILARITY_THRESHOLD = float(
    os.environ.get("IMAGE_SIMILARITY_THRESHOLD") or 0.75)


class ImageRecognitionAppiumTest(BitBarAppiumTest):
    image_dir = None
    rrpm = None

    states = set()
    last_state = None

    def setUp(self, **kwargs):
        super(ImageRecognitionAppiumTest, self).setUp(**kwargs)
        self.image_dir = _create_dir_if_not_exist(_image_dir, 'images')
        self.rrpm = IMAGE_REFRESH_RATE  # per minute

    ########################################
    # template matching
    ########################################

    def find_occurrrence(self, partial_image_path) -> None:
        screenshot = self.driver.get_screenshot_as_base64()
        with open(partial_image_path, "rb") as f:
            partial_image = base64.b64encode(f.read()).decode('UTF-8')
        try:
            result = self.driver.find_image_occurrence(
                screenshot,
                partial_image,
                threshold=IMAGE_OCCURRENCE_THRESHOLD)
        except WebDriverException as e:
            if 'Cannot find any occurrences' in str(e):
                log('No template found in screenshot')

        rect = result['rect']
        x, y, w, h = rect['x'], rect['y'], rect['width'], rect['height']
        log(f'Occurrence complete, result [x={x}, y={y}] and [w={w}, h={h}]')
        return rect

    def test_find_occurrrence_cv2(self):
        log(f'Test find image occurence at')

        full_image_path = self.save_screenshot(
            header='cv2', include_time=True)
        template = cv2.imread('images/asset/button-start.png', 0)
        image = cv2.imread(full_image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        log('match complete')

        height, width = template.shape[:2]

        top_left = max_loc
        bottom_right = (top_left[0] + width, top_left[1] + height)
        log(f'Cord    top left [{top_left[0]:4}, {top_left[1]}:4]')
        log(f'Cord bottom right[{bottom_right[0]:4}, {bottom_right[1]}:4]')
        cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 5)
        log('locate complete')

    ########################################
    # match similar
    ########################################

    def find_similarity(self, path_iterable):
        highest = 0
        highest_path = None
        screenshot = self.driver.get_screenshot_as_base64()
        for path in path_iterable:
            with open(path, "rb") as f:
                preload_screenshot = base64.b64encode(f.read()).decode('UTF-8')
            try:
                result = self.driver.get_images_similarity(
                    screenshot,
                    preload_screenshot)
                if result['score'] > highest:
                    highest = result['score']
                    highest_path = path
                    if highest > IMAGE_SIMILARITY_THRESHOLD:
                        break
            except WebDriverException as e:
                log(str(e))
            # log(
            #     f'Similarity with {path}, score = {result["score"]:.4}/{highest:.4}')

        log(f'Highest similarity score = {highest}, image {highest_path}')
        return path

    def test_similarity_cv2(self):
        pass

    ########################################
    # match features
    ########################################

    def test_feature(self):
        self.driver.match_images_features()

    def test_feature_cv2(self):
        pass

    def _destroy_file(self, path):
        pass

    async def _destroy_file():
        pass


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
