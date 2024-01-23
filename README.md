# zhaoge-cards

This project is dedicated to run automated UI scripts on [Cards! Ahoy](https://cardsahoy.metalist.io/) to minimize
human factor in the game. Inspired from this BitBar github [subfolder](https://github.com/bitbar/test-samples/tree/master/samples/testing-frameworks/appium/server-side/python).

## Apps

You will need these necessary applications to run the project:
 - Emulator: specifically `adb`, should comes with emulator.
 - Emulated Android: have Cards Ahoy! pre-installed.
 - Python: preferably conda (python environemnt provision).

## Folder Content

This folder contains the following files:

* `BitBarAppiumTest.py` and `BitBarSampleAppTest.py` are the actual
  test files written in Python. The test execution uses Python's
  unittest framework for test execution.

* `requirements.txt` lists the required Python packages that need to be
  installed for the test to be executable, e.g. AppiumPythonClient.

* `prepare.sh` prepares the environment so so the script `run.sh` is runnable from command line.