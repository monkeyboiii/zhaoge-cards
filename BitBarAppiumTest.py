# -*- coding: UTF-8 -*-

#
# Copyright(C) 2023 SmartBear Software
#
#
# NOTE: This is very much work in progress
#
__author__ = 'Henri Kivelä <henri.kivela@bitbar.com>, Lasse Häll <lasse.hall@bitbar.com>'


from typing import Optional
import os
import pprint
import unittest
import threading

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

from misc import log, _create_dir_if_not_exist


SCREENSHOT_MAX_COUNT = 1000  # in seconds
SCREENSHOT_CLEANER_INTERVAL = 60 * 120  # in seconds


class BitBarAppiumTest(unittest.TestCase):
    # Appium
    driver = None

    appium_server_url = None
    screenshot_dir = None
    # _screenshot_count = 0

    _capabilities = None

    ########################################
    # unittest
    ########################################

    def setUp(self,
              appium_server_url=None,
              screenshot_dir=None,

              platform_name=None,
              platform_version=None,
              automation_name=None,
              auto_grant_permission=None,

              udid=None,
              device_name=None,
              app_package=None,
              app_activity=None,

              full_reset=None,
              no_reset=None,

              bundle_id=None,
              application_file=None,
              browser_name=None
              ):
        # Setup fields
        self.appium_server_url = appium_server_url or os.environ.get(
            'APPIUM_URL') or 'http://127.0.0.1:4723'
        self.screenshot_dir = _create_dir_if_not_exist(
            screenshot_dir or 'screenshots', 'screenshots')
        self._capabilities = {
            "platformName": platform_name or os.environ.get('APPIUM_PLATFORM_NAME') or 'Android',
            "appium:platformVersion": platform_version or os.environ.get("APPIUM_PLATFORM_VERSION") or "13",
            "appium:automationName": automation_name or os.environ.get("APPIUM_AUTOMATION") or "UiAutomator2",
            "appium:autoGrantPermissions": auto_grant_permission or os.environ.get("APPIUM_PERMISSION") or True,

            "appium:deviceName": device_name or os.environ.get('APPIUM_DEVICE') or "Pixel 7 API 34",
            "appium:udid": udid or os.environ.get("APPIUM_UDID") or "emulator-5554"
        }

        bundle_id = bundle_id or os.environ.get('APPIUM_BUNDLEID')
        application_file = application_file or os.environ.get('APPIUM_APPFILE')
        browser_name = browser_name or os.environ.get('APPIUM_BROWSER')
        app_package = app_package or os.environ.get('APPIUM_PACKAGE')
        app_activity = app_activity or os.environ.get('APPIUM_ACTIVITY')

        if bundle_id is not None:
            # IOS
            log(f'Using bundleId {self.bundle_id}')
            self._capabilities['appium:bundleId'] = self.bundle_id
        elif application_file is not None:
            log(f'Using application file {self.application_file}')
            self._capabilities['appium:app'] = self.application_file
        elif browser_name is not None:
            log(f'Using mobile browser {self.browser_name}')
            self._capabilities['browserName'] = self.browser_name
        elif app_package is not None and app_activity is not None:
            # Android
            log(f'Using preinstalled app {app_package.split(".")[-1]}')
            self._capabilities['appium:appPackage'] = app_package
            self._capabilities['appium:appActivity'] = app_activity
        else:
            log(f'No application selected in particular')

        if full_reset is not None:
            self._capabilities['appium:fullReset'] = full_reset
        if no_reset is not None:
            self._capabilities['appium:noReset'] = no_reset

        log(f'Got desired capabilities:\n{pprint.pformat(self._capabilities)}')

        # Initialize WebDriver
        log(f'Connecting WebDriver to {self.appium_server_url}')
        self.driver = webdriver.Remote(
            self.appium_server_url,
            options=UiAutomator2Options().load_capabilities(self._capabilities)
        )

        # Wait max 30 seconds for elements
        self.driver.implicitly_wait(30)
        log('WebDriver response received')

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    ########################################
    # utils
    ########################################

    def get_driver(self, **kwargs):
        if not self.driver:
            self.setUp(**kwargs)
        return self.driver

    def _isPlatformName(self, name: str) -> bool:
        return self._capabilities.platform_name and self._capabilities.platform_name.upper() == name.upper()

    def isAndroid(self) -> bool:
        return self._isPlatformName('ANDROID')

    def isIOS(self) -> bool:
        return self._isPlatformName('IOS')

    def _get_window_dimension(self):
        _size = self.driver.get_window_size()
        return _size["height"], _size["width"]

    ########################################
    # screen manipulation
    ########################################

    def tap(self, x: Optional[int] = None, y: Optional[int] = None):
        height, width = self._get_window_dimension()
        self.driver.tap([(x or width / 2, y or height / 2)])

    def swipe_down(self):
        # TODO: check this
        self.driver.find_image_occurrence()
