import os
import unittest

from ImageRecognitionAppiumTest import ImageRecognitionAppiumTest
from time import sleep

from misc import log


NO_ACTION_RUN = True

_image_dir = os.environ.get("IMAGE_RECOGNITION_DIR") or 'images'

IMAGE_FILE_DIR = dict(
    startButton=os.path.join(_image_dir, 'asset', 'button-start.png'),
    cancelAgeButton=os.path.join(
        _image_dir, 'asset', 'button-cancel-age-red.png'),
    confirmButton=os.path.join(_image_dir, 'asset', 'button-confirm.png'),

    rateUsPrompt=os.path.join(_image_dir, 'prompt', 'rate-us.png'),

    loginScreen=os.path.join(_image_dir, 'screen', 'login.png'),
    # loginVerifyScreen=os.path.join(_image_dir, 'screen', 'login-verify.png'),
    mainScreen=os.path.join(_image_dir, 'screen', 'main.png'),
    # mainRateScreen=os.path.join(_image_dir, 'screen', 'main-rate.png'),
    # mainUnlockScreen=os.path.join(_image_dir, 'screen', 'main-unlock.png'),
    prepareBeginnerScreen=os.path.join(
        _image_dir, 'screen', 'prepare-beginner.png'),
    prepareBronzeScreen=os.path.join(
        _image_dir, 'screen', 'prepare-bronze.png'),
    # prepareSilverScreen=os.path.join(_image_dir, 'screen', 'prepare-silver.png')
    # prepareGoldScreen=os.path.join(_image_dir, 'screen', 'prepare-gold.png')
    # prepareMasterScreen=os.path.join(_image_dir, 'screen', 'prepare-master.png')
    battleScreen=os.path.join(_image_dir, 'screen', 'battle.png'),
    battleReadyScreen=os.path.join(_image_dir, 'screen', 'battle-ready.png'),
    battleSearchScreen=os.path.join(_image_dir, 'screen', 'battle-search.png'),
    battleEndScreen=os.path.join(_image_dir, 'screen', 'battle-end.png'),
)

capabilities = dict(
    full_reset=False,
    no_reset=True,
    app_package=None if NO_ACTION_RUN else os.environ.get('APPIUM_PACKAGE'),
    app_activity=None if NO_ACTION_RUN else os.environ.get('APPIUM_ACTIVITY')
)


class CardsAhoyAppiumTest(ImageRecognitionAppiumTest):
    def setUp(self):
        super(CardsAhoyAppiumTest, self).setUp(
            **capabilities
        )

    def test_login(self):
        log('Test login start')
        log('wait for 30 seconds for loading before action')

    def test_swipe(self):
        log("Test swipe start")
        self.swipe_down()

    def test_find_most_similar_image(self):
        log('Test find_most_similar_image')
        screen_path_iterable = set(IMAGE_FILE_DIR[key] for key in
                                   filter(lambda s: s.endswith("Screen"), IMAGE_FILE_DIR.keys()))
        log(f'size = {len(screen_path_iterable)}')
        log(self.find_similarity(screen_path_iterable))


if __name__ == '__main__':
    unittest.main()
