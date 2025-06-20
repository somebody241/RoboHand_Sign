import whisper
import sounddevice as sd
import numpy as np
import keyboard
import map
import code

alphabet = ['а', 'б', 'в', 'г', 'е', 'и', 'л', 'м', 'н', 'о', 'п', 'р', 'т', 'у', 'х', 'ц', 'ч', 'ш', 'ю']


model = whisper.load_model("base")
sample_rate = 16000
dur = 5
running = True

print("SPACE to start/stop")
print("ESC to exit")

audio = sd.rec(int(dur * sample_rate), samplerate=sample_rate, channels=1, dtype=np.float32, frames=48000)
sd.wait()
result = model.transcribe(audio.flatten(), language="bg")
arr = list(result)
print("result: " + str(arr))
if set(arr).issubset(alphabet):
    for i in arr:
        map.table(i)
code.board.close()
