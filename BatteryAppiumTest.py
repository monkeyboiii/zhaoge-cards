import unittest

from BitBarAppiumTest import BitBarAppiumTest
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

from misc import log

capabilities = dict(
    app_package='com.android.settings',
    app_activity='.Settings',
)


class BatteryAppiumTest(BitBarAppiumTest):
    def setUp(self):
        super(BatteryAppiumTest, self).setUp(**capabilities)

    def test_find_battery(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        el.click()
        log("Sleep for 2 secs to confirm clicked")
        sleep(2)

if __name__ == '__main__':
    unittest.main()