import unittest

from BitBarAppiumTest import BitBarAppiumTest
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

from misc import log


capabilities = dict(
    full_reset=False,
    no_reset=True
)


class CardsAhoyAppiumTest(BitBarAppiumTest):
    def setUp(self):
        super(CardsAhoyAppiumTest, self).setUp(**capabilities)

    def test_login(self) -> None:
        log('Test login, wait for 30 seconds for loading before action')
        sleep(30)
        self.tap()
        log('Test login, complete')
        sleep(30)

if __name__ == '__main__':
    unittest.main()