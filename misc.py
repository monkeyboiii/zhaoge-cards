import os
import sys
from datetime import datetime


def log(msg):
    header = ''
    if os.environ.get('APPIUM_DEVICE'):
        header = f"[{os.environ.get('APPIUM_DEVICE')}] "
    print(f'[{datetime.now().strftime("%H:%M:%S.%f")[:-3]}] {header}{msg}')
    sys.stdout.flush()

def _create_dir_if_not_exist(dir_name: str, purpose='images') -> str:
    if not os.path.isabs(dir_name):
        dir_name = os.path.join(os.getcwd(), dir_name)
    log(f'Will save {purpose} at {dir_name}')
    if not os.path.exists(dir_name):
        log(f'Creating directory {dir_name}')
        os.mkdir(dir_name)
    return dir_name