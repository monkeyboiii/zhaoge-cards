import os
import unittest
from BitBarAppiumTest import BitBarAppiumTest
from misc import log, _create_dir_if_not_exist


_image_dir = os.environ.get("IMAGE_RECOGNITION_DIR")
_refresh_rate_per_minute = int(os.environ.get("IMAGE_REFRESH_RATE")) or 10


class ImageRecognitionAppiumTest(BitBarAppiumTest):
    image_dir = None
    rrpm = None

    states = set()
    last_state = None
    
    def setUp(self, **kwargs):
        super(ImageRecognitionAppiumTest, self).setUp(**kwargs)
        self.image_dir = _create_dir_if_not_exist(_image_dir or 'images', 'images')
        self.rrpm = _refresh_rate_per_minute
        
    def detectChange():
        pass

    def test_swipe(self):
        pass

if __name__ == '__main__':
    unittest.main()