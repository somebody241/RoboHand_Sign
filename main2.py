import whisper
import sounddevice as sd
import numpy as np
import map
from pyfirmata import Arduino

from sign_letters import *

# board = Arduino('/dev/cu.usbmodem1101')
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

alphabet = ['а', 'б', 'в', 'г', 'е', 'и', 'л', 'м', 'н', 'о', 'п', 'р', 'т', 'у', 'х', 'ц', 'ч', 'ш', 'ю']

left_hand_letters = ['л', 'м', 'п', 'т']

rh = right_hand
lh = left_hand

model = whisper.load_model("base")
sample_rate = 16000
dur = 3
running = True

print("SPACE to start/stop")
print("ESC to exit")

audio = sd.rec(int(dur * sample_rate), samplerate=sample_rate, channels=1, dtype=np.float32)
sd.wait()
result = model.transcribe(audio.flatten(), language="bg")['text']
arr = list(result)
for i in arr:
    if i == ' ':
        arr.remove(i)
print("result: " + str(arr))

for i in arr:
    if i in alphabet:
        if i in left_hand_letters:
            map.table[i](lh)
            map.table['stop'](rh)
        else:
            map.table[i](rh)
            map.table['stop_left'](lh)
    else:
        map.table['stop'](rh)
        map.table['stop_left'](lh)
board.exit()
