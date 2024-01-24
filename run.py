import argparse

parser = argparse.ArgumentParser(description="Run UI automation tests")
parser.add_argument('-f', '--test-file', default='CardsAhoyAppiumTest.py')
parser.add_argument('-c', '--test-case', nargs='+', default="login")


def run():
    pass


if __name__ == '__main__':
    run()
