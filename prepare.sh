# currently supports one client vm


####################
#### Appium
####################
export APPIUM_URL=http://127.0.0.1:4723
export APPIUM_PLATFORM_NAME=Android
export APPIUM_AUTOMATION=UiAutomator2
export APPIUM_PLATFORM_VERSION=13
export APPIUM_PERMISSION=true

export APPIUM_DEVICE="Pixel 7 API 34" 
export APPIUM_UDID=emulator-5554

export APPIUM_PACKAGE=com.metalist.cardsahoy
export APPIUM_ACTIVITY=com.unity3d.player.UnityPlayerActivity


####################
#### Image Recognition
####################
export IMAGE_RECOGNITION_DIR=images
export IMAGE_REFRESH_RATE=10 # per minute
export SCREENSHOT_MAX_COUNT=1000
export SCREENSHOT_CLEANER_INTERVAL=100 # seconds