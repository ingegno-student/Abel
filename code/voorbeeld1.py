from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(0)

sense.show_message("hello", text_colour=(0, 250, 0), back_colour=(255, 165, 0)) 

sense.set_pixel(3, 3, (255, 255, 255))
sense.set_pixel(4, 3, (255, 255, 255))
sense.set_pixel(3, 4, (255, 255, 255))
sense.set_pixel(4, 4, (255, 255, 255))
