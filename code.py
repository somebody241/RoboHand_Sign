from pyfirmata import Arduino
import time

board = Arduino('COM9')

right_pinky = board.get_pin("d:2:s")
right_ring = board.get_pin("d:4:s")
right_middle = board.get_pin("d:3:s")
right_index = board.get_pin("d:5:s")
right_thumb = board.get_pin("d:6:s")

left_pinky = board.get_pin("d:8:s")
left_ring = board.get_pin("d:9:s")
left_middle = board.get_pin("d:10:s")
left_index = board.get_pin("d:11:s")
left_thumb = board.get_pin("d:12:s")

for angle in range(30, 150, 10):
    left_pinky.write(angle)
    time.sleep(0.1)
    left_ring.write(angle)
    time.sleep(0.1)
    left_middle.write(angle)
    time.sleep(0.1)
    left_index.write(angle)
    time.sleep(0.1)
    left_thumb.write(angle)
    time.sleep(0.1)

# for angle in range(150, 30, -10):
#     right_pinky.write(angle)
#     time.sleep(0.1)
#     right_ring.write(angle)
#     time.sleep(0.1)
#     right_middle.write(angle)
#     time.sleep(0.1)
#     right_index.write(angle)
#     time.sleep(0.1)
#     right_thumb.write(angle)
#     time.sleep(0.1)
#
#     left_pinky.write(angle)
#     time.sleep(0.1)
#     left_ring.write(angle)
#     time.sleep(0.1)
#     left_middle.write(angle)
#     time.sleep(0.1)
#     left_index.write(angle)
#     time.sleep(0.1)
#     left_thumb.write(angle)
#     time.sleep(0.1)

board.exit()