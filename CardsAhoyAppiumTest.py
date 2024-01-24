import unittest

from BitBarAppiumTest import BitBarAppiumTest
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

from misc import log


capabilities = dict(
    full_reset=False,
    no_reset=True
)

no_app_capabilities = dict(
    app_package=None,
    app_activity=None
)


class CardsAhoyAppiumTest(BitBarAppiumTest):
    def setUp(self):
        super(CardsAhoyAppiumTest, self).setUp(
            **capabilities,
            **no_app_capabilities
        )

    def test_login(self):
        log('Test login start')
        log('wait for 30 seconds for loading before action')
        sleep(30)
        self.tap()
        log('Test login, complete')

    def test_swipe(self):
        log("Test swipe start")
        self.swipe_down()

    def test_auto_play(self):
        '''This test assumes battle has already started'''
        log('Test auto play start')


if __name__ == '__main__':
    unittest.main()
