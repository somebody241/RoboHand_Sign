import whisper
import sounddevice as sd
import numpy as np
import keyboard
import map
import code

alphabet = ['а', 'б', 'в', 'г', 'е', 'и', 'л', 'м', 'н', 'о', 'п', 'р', 'т', 'у', 'х', 'ц', 'ч', 'ш', 'ю']


model = whisper.load_model("base")
sample_rate = 16000
running = True

print("SPACE to start/stop")
print("ESC to exit")


while True:
    try:
        while True:
            if running:
                audio = sd.rec(samplerate=sample_rate, channels=1, dtype=np.float32, frames=48000)
            else:
                sd.stop()
                result = model.transcribe(audio.flatten(), language="bg")
                print("result: "+result)
                arr = list(result)
                if set(arr).issubset(alphabet):
                    for i in arr:
                        print(map.table(i))
            if keyboard.is_pressed('space'):
                running = not running
    except KeyboardInterrupt:
        print("Program interrupted.")
    if keyboard.is_pressed('esc'):
        break

code.board.close()