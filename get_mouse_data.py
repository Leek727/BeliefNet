import mss
import mss.tools
import cv2
import numpy
import json
import time
from threading import Timer
from pynput.keyboard import Listener
from pynput import *


mouse_controller=mouse.Controller()

# The screen part to capture
monitor = {"top": 180, "left": 510, "width": 900, "height": 900}
output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
scale = (int(monitor['width']/10),int(monitor['height']/10))

index = 23822
while True:
    # -------------------------- screenshot image --------------------------
    # Grab the data
    sct = mss.mss()
    im = sct.grab(monitor)
    im = numpy.array(im)
    im = numpy.flip(im[:, :, :3], 2)  # 1
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # 2

    # resize
    im = cv2.resize(im, scale, interpolation = cv2.INTER_AREA)
    
    # -------------------------- save image --------------------------
    #             w,a,s,d  x,y
    pos = mouse_controller.position
    keypresses = [pos[0],pos[1]]
    json_data = {
        "image":[int(x) for x in im.flatten()],
        "pos":keypresses
    }
    with open(f'dataset/{index}.json', 'w') as f:
        json.dump(json_data, f)
    
    
    cv2.imshow("", cv2.resize(im, (scale[0]*5, scale[1]*5), interpolation = cv2.INTER_AREA))



    # wait
    time.sleep(0.05)
    index += 1
    
    # exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()