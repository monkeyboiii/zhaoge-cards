#!/bin/bash

#######################
#### conda
#######################

OS_TYPE=$(uname)
CONDA_INSTALLED=0


if ! commmand -v python &> /dev/null; then
    echo "Install conda first on  ${OS_TYPE}"
    exit 1
else
    echo "${OS_TYPE} has conda installed"
    CONDA_INSTALLED=1
fi


if [ "$OS_TYPE" == "Darwin" ]; then
    echo "Running on macOS"
elif [ "$OS_TYPE" == "Linux" ]; then
    echo "Running on Linux"
elif [ "$OS_TYPE" == "Windows" ]; then
    echo "Running on Windows"
else
    echo "Unknown operating system: $OS_TYPE"
fi


#################
#### Appium
####################
export APPIUM_INSTANCE_COUNT=${1:-6}


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
export SCREENSHOT_CLEANER_INTERVAL=120 # seconds

