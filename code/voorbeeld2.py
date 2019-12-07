from sense_hat import SenseHat

import time
import random
sense = SenseHat()
sense.set_rotation(270)

#sense.show_message("hello", text_colour=(0, 250, 0), back_colour=(255, 165, 0)) 

for i in range(100):
  xpos = random.randint(0,7)
  ypos = random.randint(0,7)
 
  color =  random. randint(1, 3)
  if color == 1:
    sense.set_pixel(xpos, ypos, (0, random.randint(100, 255), random.randint(100,255)))
  elif color == 2:
    sense.set_pixel(xpos, ypos, (random. randint(100, 255), 0, random.randint(100,255)))
  else:
    sense.set_pixel(xpos, ypos, (random.randint(100, 255), random.randint(100,255), 0))
  time.sleep(0.2)
