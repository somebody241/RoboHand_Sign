from pyfirmata import Arduino

from sign_letters import *

board = Arduino('COM7')

right_pinky = board.get_pin("d:2:s")
right_ring = board.get_pin("d:4:s")
right_middle = board.get_pin("d:3:s")
right_index = board.get_pin("d:5:s")
right_thumb = board.get_pin("d:6:s")

left_pinky = board.get_pin("d:11:s")
left_ring = board.get_pin("d:8:s")
left_middle = board.get_pin("d:9:s")
left_index = board.get_pin("d:12:s")
left_thumb = board.get_pin("d:10:s")

right_hand = Hand([right_pinky, right_ring, right_middle, right_index, right_thumb])

left_hand = Hand([left_pinky, left_ring, left_middle, left_index, left_thumb])

board.exit()
