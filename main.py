# import whisper
# import sounddevice as sd
# import numpy as np
#
# model = whisper.load_model("base")
# sample_rate = 16000
# duration = 5
# print("Recording...")
# audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.float32)
# sd.wait()
#
# result = model.transcribe(audio.flatten(), language="bg")
# print("Transcription:", result["text"])


import keyboard
import time

running = False

print("SPACE to start")
print("ESC to exit")

try:
    while True:
        if running:
            # Your code that you want to loop goes here
            print("Running...")
            time.sleep(1)  # Simulate some work being done
        else:
            time.sleep(0.1)  # Small delay to prevent high CPU usage when idle

        if keyboard.is_pressed('esc'):
            print("Exiting program.")
            break
except KeyboardInterrupt:
    print("Program interrupted.")
finally:
    keyboard.unhook_all()
