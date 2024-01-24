import cv2
import numpy as np
from misc import log

image = cv2.imread('images/screen/main-page.png')
log('read complete')
# cv2.imshow('main-page', image)
# log('show complete')
# cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
log('gray complete')
template = cv2.imread('images/asset/start.png', 0)
log('read 2 complete')


result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
log('match complete')

height, width = template.shape[:2]

top_left = max_loc
bottom_right = (top_left[0] + width, top_left[1] + height)
log(f'Cord [{top_left[0]}, {top_left[1]}]')
log(f'Cord [{bottom_right[0]}, {bottom_right[1]}]')
cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 5)
log('locate complete')

cv2.imshow('main-page-2', image)
log('complete')
cv2.waitKey(0)
cv2.destroyAllWindows()
