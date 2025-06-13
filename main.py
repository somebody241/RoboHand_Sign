import whisper
import sounddevice as sd
import numpy as np
import keyboard
import time

model = whisper.load_model("base")
sample_rate = 16000
running = False

print("SPACE to start/stop")
print("ESC to exit")

while True:
    try:
        while True:
            if running:
                print("Running")
            else:
                print("Not running")
            if keyboard.is_pressed('space'):
                running = not running
    except KeyboardInterrupt:
        print("Program interrupted.")
    if keyboard.is_pressed('esc'):
        break

    # audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.float32)
    # sd.wait()
    # result = model.transcribe(audio.flatten(), language="bg")
